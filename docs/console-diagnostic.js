// 把这段整段复制 → 后台页面的 Console 里粘贴运行，把输出发回来
(async () => {
  const readTok = () => {
    const c = Object.fromEntries(document.cookie.split('; ').map(s => s.split('=')));
    return decodeURIComponent(c['keystatic-gh-access-token'] || '');
  };
  console.log('== 1) cookie 里的 token ==');
  console.log('存在:', !!readTok(), '| 前缀:', readTok().slice(0, 4), '| 长度:', readTok().length);

  console.log('== 2) 刷新端点 ==');
  const rt = await fetch('/api/keystatic/github/refresh-token', { method: 'POST' });
  console.log('refresh-token ->', rt.status);

  const token = readTok();
  console.log('刷新后 token 前缀:', token.slice(0, 4), '| 长度:', token.length);
  if (!token) { console.log('❌ 会话失效：拿不到令牌，这就是 0 entries 的原因'); return; }

  console.log('== 3) GraphQL（Keystatic 同款查询，oid 挂在 target 上）==');
  const gh = await fetch('https://api.github.com/graphql', {
    method: 'POST',
    headers: { Authorization: 'Bearer ' + token, 'Content-Type': 'application/json' },
    body: JSON.stringify({ query: `query{viewer{login} repository(owner:"xyeah126",name:"china-sf"){ id defaultBranchRef{ id name } refs(refPrefix:"refs/heads/",first:100){ nodes{ name target{ oid ... on Commit{ tree{ oid } } } } } } }` }),
  }).then(r => r.json());
  console.log('viewer:', gh?.data?.viewer?.login, '| errors:', JSON.stringify(gh?.errors || null).slice(0, 300));
  const repo = gh?.data?.repository;
  const nodes = repo?.refs?.nodes || [];
  console.log('默认分支:', repo?.defaultBranchRef?.name, '| refs 数:', nodes.length);
  if (!repo) { console.log('❌ GraphQL 拿不到仓库 → 见上方 errors'); return; }

  const branchNode = nodes.find(n => n.name === repo.defaultBranchRef?.name) || nodes[0];
  const sha = branchNode?.target?.tree?.oid;
  console.log('分支树 sha:', sha);
  if (!sha) { console.log('❌ 拿不到 tree oid，refs 原始数据:', JSON.stringify(nodes).slice(0, 400)); return; }

  console.log('== 4) REST git/trees（拿文件列表）==');
  const tree = await fetch('https://api.github.com/repos/xyeah126/china-sf/git/trees/' + sha + '?recursive=1', { headers: { Authorization: 'Bearer ' + token } }).then(r => r.json());
  const all = tree.tree || [];
  console.log('HTTP 层 message:', tree.message || '无 | truncated:', tree.truncated, '| 总条目:', all.length);
  console.log('works/zh 条目:', all.filter(e => e.path.startsWith('src/content/works/zh/')).length);
  console.log('pages 条目:', all.filter(e => e.path.startsWith('src/content/pages/')).length);
  console.log('✅ 全链路通，条目应该能显示（刷新页面试试）');
})();
