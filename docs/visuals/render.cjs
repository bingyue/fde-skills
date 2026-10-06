#!/usr/bin/env node
/** Rebuild the editable diagrams and PNG previews. Requires Playwright + Chromium. */
const fs = require('node:fs/promises');
const path = require('node:path');
const { chromium } = require('playwright');

const OUT = path.resolve(__dirname, '../assets/visuals');
const W = 1600, H = 900;
const C = { bg: '#FFFCF7', white: '#FFFFFF', ink: '#17213A', muted: '#657083',
  orange: '#E7652D', pale: '#FFF0E4', blue: '#285F9B', bluePale: '#EDF3FA',
  green: '#547568', greenPale: '#EEF4EF', line: '#D9DFE5' };
const esc = s => String(s).replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;').replaceAll('"', '&quot;');
const rect = (x,y,w,h,fill=C.white,stroke=C.line,r=0) => `<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="${r}" fill="${fill}" stroke="${stroke}"/>`;
const line = (x1,y1,x2,y2,color=C.line,width=2) => `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="${color}" stroke-width="${width}"/>`;
const arrow = (points,color=C.blue,dashed=false) => `<path d="${points}" fill="none" stroke="${color}" stroke-width="2.5" ${dashed?'stroke-dasharray="7 6"':''} marker-end="url(#arrow-${color===C.orange?'orange':color===C.green?'green':'blue'})"/>`;
function text(x,y,lines,{size=24,color=C.ink,weight=400,max=1488,gap=size*1.4,anchor='start'}={}) {
  lines = Array.isArray(lines)?lines:[lines];
  return lines.map((t,i)=>`<text x="${x}" y="${y+i*gap}" font-size="${size}" font-weight="${weight}" fill="${color}" text-anchor="${anchor}" data-max-width="${max}">${esc(t)}</text>`).join('');
}
function page(lang,num,title,subtitle,source,body) {
  return `<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}" role="img" aria-labelledby="title desc">
<title id="title">${esc(title)}</title><desc id="desc">${esc(subtitle)}. ${esc(source)}. 邴越 · FDE前线 · FDEChina.ai</desc>
<defs>${['blue','orange','green'].map(k=>`<marker id="arrow-${k}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="${C[k]}"/></marker>`).join('')}</defs>
<g font-family="'PingFang SC', 'Noto Sans CJK SC', 'Microsoft YaHei', Arial, sans-serif">
${rect(0,0,W,H,C.bg,C.bg)}
${text(56,47,'FDE FRONTLINE / FDE SKILLS',{size:16,weight:600,color:C.muted})}
${text(1544,47,lang==='zh'?'企业 AI 交付框架':'ENTERPRISE AI DELIVERY',{size:16,color:C.muted,anchor:'end'})}
${text(56,112,title,{size:42,weight:650})}
${text(56,160,subtitle,{size:23,color:C.muted})}
${line(56,192,1544,192)}${line(56,192,140,192,C.orange,5)}
${body}
${line(56,804,1544,804)}
${text(56,831,source,{size:15,color:C.muted})}
${text(56,867,'邴越 · FDE前线 · FDEChina.ai',{size:18,weight:600})}
${text(1544,867,`${num} / 04`,{size:16,color:C.muted,anchor:'end'})}
</g></svg>\n`;
}
function delivery(lang) {
  const zh = lang==='zh';
  const cards = zh ? [
    ['理解业务','Discovery · Diagnosis',['现状流程','问题与机会优先级'],'业务价值与负责人'],
    ['定义方案','Solution · Architecture',['PoC 范围','系统与权限边界'],'可行性与验收标准'],
    ['构建验证','Build · Eval',['可运行增量','评测报告与失败分析'],'质量、成本与安全'],
    ['上线交付','Deploy · Delivery',['运行与回滚手册','生产验收与责任接管'],'可运行、可回滚、可接管'],
  ] : [
    ['Understand','Discovery · Diagnosis',['Observed workflow','Prioritized opportunities'],'Value and accountable owner'],
    ['Design','Solution · Architecture',['PoC scope','System and access scope'],'Feasibility and acceptance'],
    ['Build & verify','Build · Eval',['Runnable increment','Eval and failure report'],'Quality, cost and safety'],
    ['Deliver','Deploy · Delivery',['Operations and rollback','Acceptance and handover'],'Operability and ownership'],
  ];
  let b='';
  cards.forEach((c,i)=>{
    const x=56+i*380;
    b+=rect(x,238,348,348);
    b+=rect(x,238,348,5,i===3?C.green:C.orange,'none');
    b+=text(x+24,283,`0${i+1}`,{size:20,color:i===3?C.green:C.orange,weight:700,max:300});
    b+=text(x+24,329,c[0],{size:31,weight:650,max:300});
    b+=text(x+24,363,c[1],{size:19,color:C.muted,max:300});
    b+=line(x+24,390,x+324,390);
    b+=text(x+24,426,zh?'阶段产物':'EVIDENCE',{size:17,color:C.muted,weight:600,max:300});
    b+=text(x+24,464,c[2],{size:23,gap:35,max:300});
    b+=rect(x+16,528,316,42,i===3?C.greenPale:C.pale,'none');
    b+=text(x+30,556,c[3],{size:zh?21:18,weight:600,max:288});
    if(i<3) b+=arrow(`M ${x+350} 412 L ${x+373} 412`,C.orange);
  });
  b+=rect(56,629,1488,119,C.bluePale,'none');
  b+=text(80,674,zh?'每一道门槛，都需要证据、负责人和明确结论':'Every gate needs evidence, an owner and a clear decision',{size:30,weight:600,max:1436});
  b+=text(80,716,zh?'未通过 → 返回对应阶段补证据或修复，再进入下一阶段':'Failed gate → return to the relevant stage, remediate and evaluate again.',{size:23,color:C.blue,max:1436});
  return page(lang,'01',zh?'用可验证的证据，推进每一次企业交付':'Move delivery forward with verifiable evidence',zh?'8 个阶段，4 组决策门：从客户现场到生产验收':'Eight stages, four groups of gates: from field discovery to production acceptance',zh?'来源：docs/concepts/delivery-framework.md；推荐工作流，不代表自动执行引擎。':'Source: docs/concepts/delivery-framework.md. Recommended workflow; not an autonomous execution engine.',b);
}
function platform(lang) {
  const zh=lang==='zh'; let b='';
  b+=arrow('M 461 319 L 505 319',C.orange);
  b+=arrow('M 461 500 L 486 500 L 486 319 L 505 319',C.orange);
  b+=line(985,583,1031,583,C.blue,2.5)+line(1031,283,1031,619,C.blue,2.5);
  for(const y of [283,395,507,619]) b+=arrow(`M 1031 ${y} L 1053 ${y}`);
  b+=rect(56,238,405,165)+rect(56,429,405,243);
  b+=text(80,279,zh?'60 个核心 Skills':'60 core Skills',{size:28,weight:650,max:357});
  b+=text(80,321,['SKILL.md','Markdown + YAML Front Matter'],{size:22,gap:34,color:C.blue,max:357});
  b+=text(80,459,zh?'5 个行业 Packs':'5 industry packs',{size:28,weight:650,max:357});
  b+=text(80,502,zh?['引用通用 Skill','追加知识、约束与指标','保留核心约束']:['Reference core Skills','Add knowledge, rules and metrics','Keep core constraints'],{size:22,gap:36,max:357});
  b+=rect(80,621,357,30,C.pale,'none');
  b+=text(91,643,zh?'单一来源 · 避免复制工作流':'ONE SOURCE · REUSABLE WORKFLOWS',{size:16,weight:600,color:C.orange,max:335});
  b+=rect(510,238,475,434,C.bluePale,'none');
  b+=text(534,277,zh?'轻量 CLI 与标准化工具链':'A lightweight CLI toolchain',{size:26,weight:650,max:427});
  const steps=zh?[
    ['fde validate','Schema · 示例 · 链接 · 重复检查'],
    ['fde registry build','生成可搜索的 skills.json'],
    ['fde export <agent>','组合契约，复制资源与许可声明'],
  ]:[
    ['fde validate','Schema, examples, links, duplicates'],
    ['fde registry build','Generate searchable skills.json'],
    ['fde export <agent>','Compose contracts, assets and notices'],
  ];
  steps.forEach((s,i)=>{const y=304+i*116;b+=rect(534,y,427,95,C.white,'none');b+=text(554,y+34,s[0],{size:25,weight:600,max:387});b+=text(554,y+69,s[1],{size:20,color:C.muted,max:387});if(i<2)b+=arrow(`M 747 ${y+97} L 747 ${y+110}`,C.orange);});
  [['Codex','.agents/skills/'],['Claude Code','.claude/skills/'],['Cursor','.cursor/skills/'],['OpenCode','.opencode/skills/']].forEach((s,i)=>{
    const y=238+i*112;b+=rect(1060,y,484,90);b+=rect(1060,y,5,90,C.blue,'none');
    b+=text(1084,y+36,s[0],{size:27,weight:650,max:436});b+=text(1084,y+69,s[1],{size:21,color:C.muted,max:436});
  });
  b+=rect(56,711,1488,56,C.pale,'none');
  b+=text(80,748,zh?'导出内容：原生 Skill + 完整 FDE 契约 + 示例与模板 + LICENSE / NOTICE':'Exported: native Skill + full FDE contract + examples and templates + LICENSE / NOTICE',{size:24,weight:500,max:1440});
  return page(lang,'02',zh?'一份标准源定义，服务四类 AI Coding Agent':'One canonical source, four AI coding agents',zh?'核心 Skill 与行业上下文分开维护，通过校验、索引与适配连接到客户端':'Maintain core Skills and industry context separately; validate, index and export them to clients',zh?'来源：src/fde_skills/、schemas/、adapters/；展示仓库已实现的导出机制，不代替客户端运行验证。':'Sources: src/fde_skills/, schemas/, adapters/. Implemented export mechanism; client runtime validation remains separate.',b);
}
function industries(lang) {
  const zh=lang==='zh'; let b='';
  const xs=[56,256,676,1104], widths=[200,420,428,440];
  const heads=zh?['行业','业务任务','行业扩展','验收证据']:['INDUSTRY','BUSINESS TASK','INDUSTRY CONTEXT','ACCEPTANCE EVIDENCE'];
  const rows=zh?[
    ['电商',['商品咨询','订单与售后分流'],['SKU、政策版本、订单权限'],['规格正确、来源可查','订单数据不越权']],
    ['外贸',['询盘分析','多语言跟进与邮件草稿'],['产品资料、币种与交易条件'],['参数可追溯','邮件发送需授权']],
    ['制造',['设备问答','SOP 与维修辅助'],['设备型号、手册版本、安全前提'],['引用匹配设备版本','高风险操作转人工']],
    ['医美',['项目咨询','预约与到店分流'],['服务知识、咨询边界、转接规则'],['不作诊断或疗效承诺','专业问题转专业人员']],
    ['招聘',['岗位需求','候选人证据与面试辅助'],['岗位标准、隐私、人工复核'],['判断回链岗位证据','录用决策保留人工']],
  ]:[
    ['Ecommerce',['Product questions','Order and return triage'],['SKU, policy version,','order-level access'],['Correct specifications and sources','No unauthorized order access']],
    ['Foreign trade',['Inquiry analysis','Multilingual follow-up drafts'],['Product references, currency,','commercial terms'],['Traceable product parameters','Authorized outbound email']],
    ['Manufacturing',['Equipment questions','SOP and maintenance support'],['Equipment model, manual version,','safety preconditions'],['Version-matched citations','Human review for risky actions']],
    ['Medical beauty',['Service consultation','Booking and visit routing'],['Service facts, consultation limits,','professional escalation'],['No diagnosis or outcome promise','Escalate professional questions']],
    ['Recruitment',['Role requirements','Candidate evidence and interviews'],['Job criteria, privacy,','human review'],['Job-relevant evidence','Human hiring decisions']],
  ];
  b+=rect(56,234,1488,58,C.ink,'none');
  heads.forEach((h,i)=>b+=text(xs[i]+20,271,h,{size:19,weight:600,color:C.white,max:widths[i]-40}));
  rows.forEach((row,r)=>{
    const y=292+r*92;b+=rect(56,y,1488,92,r%2?C.bluePale:C.white,'none');b+=rect(56,y,200,92,C.pale,'none');
    const nameLines=!zh&&row[0]==='Medical beauty'?['Medical','beauty']:!zh&&row[0]==='Foreign trade'?['Foreign','trade']:[row[0]];
    b+=text(76,y+(nameLines.length===1?53:37),nameLines,{size:zh?27:19,gap:28,weight:650,max:160});
    for(let i=1;i<4;i++)b+=text(xs[i]+20,y+(row[i].length===1?53:36),row[i],{size:zh?23:20,gap:31,max:widths[i]-40});
  });
  return page(lang,'03',zh?'通用交付方法，在五类行业形成具体工作流':'Turn a shared delivery method into industry workflows',zh?'行业包追加知识、约束和指标；通用 Skill 持续复用':'Packs add knowledge, constraints and metrics while reusing core Skill workflows',zh?'来源：industries/*/pack.yaml；场景与验收方向示意，非已验证的客户收益或生产效果。':'Source: industries/*/pack.yaml. Illustrative tasks and acceptance boundaries, not verified customer outcomes.',b);
}
function knowledge(lang) {
  const zh=lang==='zh';let b='';
  b+=text(56,233,zh?'请求路径':'REQUEST PATH',{size:16,color:C.orange,weight:650});
  const nodes=zh?[
    ['业务用户','明确任务与范围'],['身份与权限','租户 / 角色 / 对象'],['任务编排','上下文与转接策略'],['检索与引用','权限过滤 / 版本匹配'],['回答或转人工','有据回答 / 无据拒答'],
  ]:[
    ['Business user','Task and scope'],['Identity & access','Tenant / role / object'],['Task orchestration','Context and escalation'],['Retrieve & cite','Access and version filters'],['Answer or escalate','Evidence or abstention'],
  ];
  nodes.forEach((n,i)=>{const x=56+i*307;b+=rect(x,262,260,137,i===4?C.greenPale:C.white);b+=rect(x,262,260,4,i===4?C.green:C.orange,'none');b+=text(x+18,313,n[0],{size:zh?26:22,weight:600,max:224});b+=text(x+18,357,n[1],{size:zh?21:18,color:C.muted,max:224});if(i<4)b+=arrow(`M ${x+264} 330 L ${x+298} 330`,C.orange);});
  b+=rect(56,479,858,218,C.bluePale,'none');
  b+=text(80,521,zh?'知识准备：保留来源、权限与有效版本':'Knowledge preparation: provenance, access and versions',{size:zh?27:26,weight:600,max:810});
  const sources=zh?[['权威资料','客户批准的知识源'],['治理与切块','清洗 / 版本 / 权限'],['可检索索引','保留来源与元数据']]:[['Trusted sources','Approved customer data'],['Govern & chunk','Clean / version / access'],['Searchable index','Sources and metadata']];
  sources.forEach((s,i)=>{const x=80+i*285;b+=rect(x,556,240,106,C.white,'none');b+=text(x+16,595,s[0],{size:zh?25:22,weight:600,max:208});b+=text(x+16,635,s[1],{size:zh?21:16.5,color:C.muted,max:208});if(i<2)b+=arrow(`M ${x+244} 609 L ${x+276} 609`);});
  b+=arrow('M 892 609 L 942 609 L 942 443 L 1107 443 L 1107 405');
  b+=text(804,432,zh?'已授权的检索上下文':'Authorized retrieval context',{size:18,color:C.blue,max:285});
  b+=rect(970,479,574,218,C.greenPale,'none');
  b+=text(994,521,zh?'评测与观测闭环':'Evaluation and observability',{size:27,weight:600,max:526});
  b+=text(994,569,zh?['离线评测 → 发布门槛 → 线上观测','失败样本 → 回归评测 → 调整方案']:['Offline eval → release gates → monitoring','Failure cases → regression → remediation'],{size:zh?23:21,gap:40,max:526});
  b+=arrow('M 1414 405 L 1414 471',C.green,true);
  b+=text(1430,444,zh?'运行证据':'Evidence',{size:16,color:C.green,max:105});
  b+=rect(56,729,1488,43,C.pale,'none');
  b+=text(80,758,zh?'生产门槛：越权泄露为零 · 引用可追溯 · 无依据时拒答 · 高风险转人工':'Production gates: no unauthorized disclosure · traceable citations · abstention · human escalation',{size:22,weight:500,max:1440});
  return page(lang,'04',zh?'知识 Agent 的可靠性，来自检索、权限与评测闭环':'Reliable knowledge agents need access, retrieval and eval',zh?'企业知识库参考架构：运行组件由具体客户项目实现与验证':'Enterprise knowledge reference architecture: customer projects implement and validate runtime components',zh?'来源：examples/02-enterprise-knowledge-base/、rag-architecture、permission-model、rag-evaluation；参考方案。':'Sources: enterprise knowledge base example; rag-architecture, permission-model, rag-evaluation. Reference design.',b);
}
const figures=[
  ['01-交付闭环','01-delivery-framework',delivery],
  ['02-平台架构','02-platform-architecture',platform],
  ['03-行业应用地图','03-industry-applications',industries],
  ['04-知识Agent参考架构','04-knowledge-agent',knowledge],
];
async function main(){
  await fs.mkdir(OUT,{recursive:true});
  const browser=await chromium.launch({headless:true});
  try {
    const p=await browser.newPage({viewport:{width:W,height:H},deviceScaleFactor:1});
    const files=[];
    for(const [cn,en,make] of figures){
      for(const lang of ['zh','en']){
        const name=lang==='zh'?cn:en, svg=make(lang);
        await fs.writeFile(path.join(OUT,`${name}.svg`),svg);
        await p.setContent(`<!doctype html><html lang="${lang}"><meta charset="UTF-8"><style>html,body{margin:0;background:${C.bg}}svg{display:block}</style>${svg}</html>`);
        await p.evaluate(()=>document.fonts.ready);
        const overflow=await p.locator('svg text').evaluateAll(nodes=>nodes.flatMap(n=>{
          const b=n.getBBox(), limit=Number(n.dataset.maxWidth);
          return b.width>limit+1||b.x<0||b.y<0||b.x+b.width>1600||b.y+b.height>900 ? [{text:n.textContent,width:b.width,limit,x:b.x,y:b.y}] : [];
        }));
        if(overflow.length)throw Error(`${name}: text overflow ${JSON.stringify(overflow)}`);
        await p.screenshot({path:path.join(OUT,`${name}.png`)});
        files.push(`${name}.png`);
        console.log(`Rendered ${name}: ${W} x ${H}; text bounds passed`);
      }
    }
    const thumbs=['00-FDE-Skills-首图.png',...figures.map(f=>f[0]+'.png')];
    const cards=await Promise.all(thumbs.map(async f=>`<figure><img src="data:image/png;base64,${(await fs.readFile(path.join(OUT,f))).toString('base64')}"><figcaption>${esc(f)}</figcaption></figure>`));
    await p.setViewportSize({width:1648,height:1800});
    await p.setContent(`<!doctype html><html lang="zh"><meta charset="UTF-8"><style>body{margin:0;padding:32px;background:#f3f0e9;font-family:Arial,'PingFang SC',sans-serif}h1{margin:0 0 24px;color:#17213a;font-size:30px}main{display:grid;grid-template-columns:1fr 1fr;gap:24px}figure{margin:0;background:white;padding:12px}figure:first-child{grid-column:1/-1}img{width:100%;display:block}figcaption{padding:10px 0 0;font-size:16px;color:#657083}</style><h1>FDE Skills · 视觉总览 / 邴越 · FDE前线 · FDEChina.ai</h1><main>${cards.join('')}</main></html>`);
    await p.evaluate(async()=>{await document.fonts.ready;await Promise.all(Array.from(document.images).map(i=>i.decode()));});
    await p.screenshot({path:path.join(OUT,'contact-sheet.png'),fullPage:true});
    await fs.writeFile(path.join(__dirname,'render-report.json'),JSON.stringify({canvas:{width:W,height:H},diagrams:files,text_bounds:'passed',fonts:'PingFang SC / Noto Sans CJK SC / Microsoft YaHei / Arial',review:'See qa-report.md for visual inspection.'},null,2)+'\n');
  } finally { await browser.close(); }
}
main().catch(e=>{console.error(e);process.exitCode=1;});
