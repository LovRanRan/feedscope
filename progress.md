# Project 0 · feedscope — Progress Tracker

> 单文件进度板 — Dashboard + Roadmap + Logs + Repo 蓝图 + Hand-write 规矩
> 维护方式:每完成一个 commit,在 Dashboard 更新 Current,在 Logs 追加一行
> Owner: Haichuan · Start: 2026-04-28 · Reference window: Phase 1 收尾(**仅参考,不绑日期**,见 Core Principle #2)

---

## 🔒 Core Principles(不可让步 · 写在最前面)

1. **Resume-grade ownership — 所有 production code 由 Haichuan 亲手写。**
   这个项目虽然是 warm-up,但跟 Project 3-6 一样要进 GitHub / 简历,必须经得起"你这段代码自己写的吗"的追问。覆盖范围:Python(typer / Pydantic models / asyncio orchestrator / pytest)、`pyproject.toml` / `.env.example` / `.gitignore`。
   Claude 的角色 = traffic-light review(🟢/🟡/🔴)+ 方向提示 + 概念解释。**只有**在 Haichuan 自己尝试过、能精准描述卡点、且持续超过 15 min 没出口时,才允许 Claude 给最小代码示例(< 10 行)+ 解释为什么这么写。能自己想出来的就**不要**先看答案。
2. **进度按"实际完成"推进,不按日历推进。**
   Roadmap 里的 7 commit 没有截止线。下一个 commit 的开工条件 = 上一个 commit 真正 done。一个 commit "done" 的判定 = ① 代码/文档落地 ② 跑通验证(`uv run pytest` / `mypy --strict` / `ruff check` / 手动 smoke 等场景对应的最小验证)③ Logs 里有一行记录(含决策点和 lesson)④ `git commit` 已经打。四者缺一不算 done,不进入下一步。

---

## 🚪 New Chat Pickup Protocol(每次开新对话先看这里)

> 目标:新 Claude 实例 3 分钟内恢复全部上下文,**不需要**任何"下一步 checklist 文档"。

按以下顺序读 `progress.md`:

1. **Core Principles**(上一节)— 两条不可让步的规则。
2. **Dashboard**(下一节)— 当前 commit / blocker / next action。**这是"现在状态"的唯一事实源。**
3. **Logs 最近 3–5 行** — 最近发生了什么、做了什么决策、踩了什么坑。
4. **当前 Commit 的 Roadmap 复选框** — 这个 commit 还差什么。

姊妹文档:`README.md`(项目说明)、`final_checklist.md`(在 `../../final_checklist.md`,Project 0 acceptance criteria 在那里)。

⚠ **不要去找任何"下一步 / pickup checklist"独立小节** — 这类文档一旦不和 Logs 同步就会变成毒源。所有"下一步"信息**只在 Dashboard 的 `Next Action` 字段**。

---

## 🔄 Update Protocol(每次有进度变化必走 · 顺序不可乱)

每次完成一个动作(无论大小),按以下顺序更新本文件。少一步 = 没更新完,下一个 chat 可能误判。

1. **Logs 末尾追加 1 行**(先做 — 历史不可篡改)
   格式:`日期 | commit | ✅/⚠/⏸/📘 内容(含做了什么 + 验证方式 + lesson 或决策点)`。
2. **Dashboard 同步**(再做 — 反映新现在)
   - `Current Commit` 改成新的 in-progress
   - `Overall Progress` 进度块按需重画
   - `Last Activity` 一句话总结刚做完的事(带日期)
   - `Next Action` 写下一个**具体可执行**的动作
   - `Blocker` 如有变化更新
3. **Roadmap** — 关闭的复选框 `[ ]` → `[x]` + 完成日期

> 黄金法则:**Logs append-only · Dashboard 永远是 now 的快照** · 两者必须同一次更新提交。

---

## 📊 Dashboard

| Field                | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Current Commit**   | `Commit 2 — Pydantic models(in progress · 设计讨论阶段,等 Haichuan 决定字段类型)`                                                                                                                                                                                                                                                                                                                                                                                       |
| **Overall Progress** | 🟩🟦⬜⬜⬜⬜⬜ 1 / 7 commits done                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **Blocker**          | none                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **Last Activity**    | 2026-04-28 · **Commit 1 关闭**。`cli.py` hand-written(typer 3 件套占位)、Python baseline 升 3.11 → 3.14、build backend hatchling → uv_build(解决路径空格 editable bug)、三连验证全过、git first commit 已打。Overall Progress 1/7。                                                                                                                                                                                                                                       |
| **Working Mode**     | HAND-WRITE · resume-grade(Commit 1 已闭,Commit 2 起 100% 严格执行 — code 全部 Haichuan 写,Claude 只 review)|进度:完成驱动,非日历驱动                                                                                                                                                                                                                                                                                                                                |
| **Next Action**      | Commit 2 设计讨论,先决定 3 件事:(1) `Article` 字段类型 — `published_at: datetime` vs `date`(arXiv = ISO datetime / HN = unix int 转后哪个统一)、`url: HttpUrl` vs `str`、`authors: list[str]` vs `tuple[str, ...]`;(2) `FetchResult` 错误怎么表达 — `error: Optional[str]` vs Result/Either pattern vs raise exception;(3) `FetchConfig` — 用 `pydantic-settings` 接 env 还是纯 CLI 参数 / 是否支持 config file。讨论完 Haichuan 在 `src/feedscope/models.py` + `src/feedscope/config.py` 自己写,Claude 只 review。 |

---

## 🗺️ Roadmap(7 commit · 按完成推进,不绑日期)

### Commit 1 — 项目脚手架 ✅ 2026-04-28

- [x] 1.a Hand-write 决策:选 **C**(Project 0 破例,Project 1+ 严格)✅ 2026-04-28
- [x] 1.b `src/feedscope/cli.py` Haichuan 自己写(typer 3 件套占位:`Typer()` + `@app.command() hello() -> None: typer.echo(...)` + `if __name__ == "__main__": app()`)✅ 2026-04-28
- [x] 1.c `uv sync` 装环境成功(经过 Python 3.14 升级 + build backend 切换 hatchling → uv_build)✅ 2026-04-28
- [x] 1.d 三连验证:`uv run feedscope` → "Hello world!" / `mypy --strict src/` Success / `ruff check` All passed ✅ 2026-04-28
- [x] 1.e `git init` + first commit(message: "Commit 1: project scaffolding (uv + ruff + mypy strict + typer entry, py3.14)")✅ 2026-04-28
- [x] 1.f Logs 追加完成行 + Dashboard 同步 ✅ 2026-04-28

### Commit 2 — Pydantic models 🟧 in progress

- [ ] 2.a 在 `src/feedscope/models.py` 设计 `Article`(title / authors / summary / url / source / published_at)
- [ ] 2.b 加 `FetchResult`(source / articles / fetched_at / error: Optional[str])
- [ ] 2.c 在 `src/feedscope/config.py` 设计 `FetchConfig`(query / limit / sources / output_path)用 `pydantic-settings`
- [ ] 2.d 关键字段决策:`published_at` 用 `datetime` vs `date`(arXiv 是 datetime,HN 是 unix timestamp)/ `url` 用 `HttpUrl` vs `str` / `authors` 用 `list[str]` 还是 `tuple[str, ...]`
- [ ] 2.e `tests/test_models.py` 写 1-2 个 validator 测试(空 title 拒绝 / url 格式 / authors 至少 1 人)
- [ ] 2.f Commit message: "Commit 2: Pydantic models for Article + FetchResult + FetchConfig"

### Commit 3 — BaseFetcher + ArxivFetcher ⬜

- [ ] 3.a `src/feedscope/fetchers/__init__.py` 空 + `src/feedscope/fetchers/base.py` 设计 `BaseFetcher`(abc.ABC,async `fetch(query: str, limit: int) -> FetchResult`)
- [ ] 3.b 关键决策:`BaseFetcher` 是否在 `__init__` 接 `httpx.AsyncClient`(注入 vs 内建)
- [ ] 3.c `src/feedscope/fetchers/arxiv.py` 实现 `ArxivFetcher`(httpx + Atom XML parsing via `xml.etree.ElementTree`)
- [ ] 3.d `tests/test_arxiv_fetcher.py` 用 `respx` mock arxiv API,2-3 个测试(正常返回 / 空结果 / HTTP 错误)
- [ ] 3.e Commit message: "Commit 3: BaseFetcher + ArxivFetcher with respx-mocked tests"

### Commit 4 — HNFetcher + tests ⬜

- [ ] 4.a `src/feedscope/fetchers/hn.py` 实现 `HNFetcher`(httpx + JSON,`hn.algolia.com/api/v1/search?tags=story&query=...`)
- [ ] 4.b `tests/test_hn_fetcher.py` 用 `respx` mock,2 个测试
- [ ] 4.c 验证:BaseFetcher 现在有 2 个 sub-class,继承抽象 justified(不再是 over-engineering)
- [ ] 4.d Commit message: "Commit 4: HNFetcher (BaseFetcher now has 2 subclasses)"

### Commit 5 — Orchestrator + JSON exporter ⬜

- [ ] 5.a `src/feedscope/orchestrator.py` 用 `asyncio.gather` 同时跑多个 fetcher,异常隔离(`return_exceptions=True`,一个源失败不影响其他)
- [ ] 5.b 这是 acceptance criteria 里 "asyncio for at least 1 concurrent operation" 的核心证据 — 跑两个 fetcher 时 wall time < 单个最长 fetcher 时间 × 1.5
- [ ] 5.c `src/feedscope/exporter.py` 简单函数 `write_json(results: list[FetchResult], path: Path) -> None`
- [ ] 5.d `tests/test_orchestrator.py` mock 两个 fetcher,验证并发 + 异常隔离
- [ ] 5.e Commit message: "Commit 5: orchestrator (asyncio.gather) + JSON exporter"

### Commit 6 — CLI 整合 + README ⬜

- [ ] 6.a 重写 `src/feedscope/cli.py`:`feedscope fetch --query "agent" --sources arxiv,hn --limit 20 --output out.json`
- [ ] 6.b CLI 命令组织决策:单 root command(`feedscope ...`)vs sub-command(`feedscope fetch ...`)— 推荐后者,留扩展空间
- [ ] 6.c `tests/test_cli.py` 用 `typer.testing.CliRunner` 写 1-2 个 e2e 测试(--help 含 fetch / fetch with mocked fetcher 输出 JSON)
- [ ] 6.d README.md 填实际内容:Install / Usage(真 example)/ Architecture(简略图)/ Development(test/lint/typecheck 命令)
- [ ] 6.e Commit message: "Commit 6: CLI fetch command + README with usage examples"

### Commit 7 — mypy --strict + ruff 全清 + 推 GitHub ⬜

- [ ] 7.a `mypy --strict src/` 修所有报错(预计有 missing return type / Any / Optional handling)
- [ ] 7.b `ruff check src/ tests/` + `ruff format` 全清
- [ ] 7.c `pytest` 确认 ≥ 5 测试全过
- [ ] 7.d acceptance criteria 自查表:uv ✓ / 类继承 ✓(BaseFetcher → 2 子类) / mypy strict ✓ / asyncio 真并发 ✓ / Pydantic input+output ✓ / typer CLI ✓ / 5+ tests ✓ / README ✓ / public repo ≥ 5 commits ✓
- [ ] 7.e 创建 GitHub public repo(`feedscope`)+ `git remote add origin ...` + push
- [ ] 7.f Commit message: "Commit 7: mypy --strict clean + lint clean + verified acceptance"
- [ ] 7.g 在 `final_checklist.md` 把 Project 0 的 acceptance checkbox 全勾掉

---

## 📁 Repo 目录蓝图

`/Users/destiny/Desktop/AI agent Engineer/Final_checklist/Final_checklist_phase_projects/project0/`

```
project0/                                  # local wrapper, GitHub repo 名为 feedscope
├── pyproject.toml                         # uv + ruff + mypy strict + pytest
├── .gitignore
├── .python-version                        # 3.14
├── README.md
├── progress.md                            # ← 本文件
├── src/feedscope/
│   ├── __init__.py                        # __version__
│   ├── cli.py                             # ★ Commit 1 占位 → Commit 6 重写
│   ├── config.py                          # ★ Commit 2: FetchConfig
│   ├── models.py                          # ★ Commit 2: Article, FetchResult
│   ├── fetchers/
│   │   ├── __init__.py
│   │   ├── base.py                        # ★ Commit 3: BaseFetcher abc
│   │   ├── arxiv.py                       # ★ Commit 3: ArxivFetcher
│   │   └── hn.py                          # ★ Commit 4: HNFetcher
│   ├── orchestrator.py                    # ★ Commit 5: asyncio.gather
│   └── exporter.py                        # ★ Commit 5: JSON writer
└── tests/
    ├── __init__.py
    ├── test_models.py                     # ★ Commit 2
    ├── test_arxiv_fetcher.py              # ★ Commit 3
    ├── test_hn_fetcher.py                 # ★ Commit 4
    ├── test_orchestrator.py               # ★ Commit 5
    └── test_cli.py                        # ★ Commit 6
```

---

## ✅ Hand-write 规矩(Project 0 生效 · 与 Core Principle #1 联动)

> Resume-grade reminder:所有"production code"列必须能在面试时一行行讲清楚为什么这么写。Claude 起草的 README 是辅助理解工具,不是最终交付物;关键签名 / model / 算法仍由 Haichuan 亲手写。

| 类型                                              | 谁来写                                                                       |
| ------------------------------------------------- | ---------------------------------------------------------------------------- |
| Python 代码(typer / Pydantic / fetcher / asyncio) | **Haichuan**(resume code)                                                    |
| 测试代码(pytest)                                  | **Haichuan**(resume code)                                                    |
| `pyproject.toml` / `.gitignore` / `.python-version` | **Haichuan**(Claude 给结构清单)— ⚠ 已被违反一次,见 Dashboard Blocker     |
| 目录 mkdir/touch 命令                              | **Haichuan** 执行(Claude 给蓝图)                                            |
| `README.md`                                       | **Claude 起草**,Haichuan review + 关键章节(Architecture / Lessons)自己改  |
| `progress.md`(本文件)                            | **Claude 起草**,Haichuan review + maintain                                   |
| `__init__.py`(纯样板,只 `__version__` 或空)     | **Claude 起草**(无业务逻辑,豁免)                                            |

**Code review 三档**:

- 🟢 过 — 一句话 kudos
- 🟡 有问题 — 指问题 + 方向,**不给代码**
- 🔴 卡 > 15 min 且精准描述 — 允许 < 10 行最小修复示例 + 解释

**反 hand-write 的信号**(Claude 会拒绝):

- "帮我写 xxx"
- "给我整个 yyy 的完整代码"
- "我不知道怎么开始,你写个例子"

**触发"给答案"的最小条件**(必须同时满足):

1. Haichuan 已经动手尝试过(贴出错误代码 / 描述思路)
2. 卡点描述精准(不是"不知道怎么写",而是"我想用 X 做 Y,但 Z 报错 / 不通")
3. 持续 > 15 min 真的没出口
   满足后 Claude 给 < 10 行最小修复 + 解释。其他场景一律 traffic-light + 方向。

---

## 📝 Logs

| Timestamp        | Commit | Event                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ---------------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2026-04-28       | —     | Project 0 正式开工。从 `final_checklist.md` 的 Mini-Project 0 acceptance criteria 推导出 7-commit roadmap。CLI 主题选定:**异步多源抓取聚合器**(arXiv 主 + HN 辅)。项目名:**feedscope**。技术栈定档:`uv` + `httpx.AsyncClient` + `typer` + `pydantic` v2 + `xml.etree.ElementTree`(arXiv Atom)+ `respx`(test mocking)+ `mypy --strict` + `ruff`。                                                                                  |
| 2026-04-28       | 1      | ⚠ **Claude 越界 hand-write 边界**。在 Haichuan 没明确授权的情况下,Claude 直接建了 `pyproject.toml` + `.gitignore` + `.python-version` + `README.md`(骨架)+ `src/feedscope/__init__.py` + `tests/__init__.py`。按 Project 3 progress.md 的 Hand-write 规矩,前 3 个文件(pyproject / gitignore / python-version)应该 Haichuan 写,Claude 只给结构清单。`README.md` 骨架 + `__init__.py` 在 Project 3 规矩里属于 Claude 起草豁免范围,这两个不算越界。**补救等 Haichuan 决定 A/B/C 路径**(见 Dashboard Blocker)。 |
| 2026-04-28       | 1      | 📘 **Lesson — 新 project 启动时,Claude 应先确认 Hand-write 规矩是否适用,而不是默认走"我帮你脚手架"路径。** 用户上传 Project 3 progress.md 后才显式发现 Hand-write 规矩 — 但用户在更早就用一句话表达过("主要的 code 一定要我自己写,重复的你可以帮我写")。Claude 当时把这句话理解成"配置文件 = 重复",但 Project 3 规矩里 `pyproject.toml` 明确是 Haichuan 写。今后所有新 project 启动第一件事:从 progress.md 模板拷一份过来 → 在 Hand-write 规矩表里逐行确认边界 → 然后才动手。 |
| 2026-04-28       | 1.a    | ✅ **Haichuan 选 C — Project 0 破例,Project 1+ 严格。** Hand-write 越界的 3 个文件(`pyproject.toml` / `.gitignore` / `.python-version`)保留 as-is,不重写,不视为 hand-write 违规。从 Commit 2 开始 100% 严格执行规矩。**关键约束写入 memory(`feedback_progress_md_workflow.md`)**:Project 1 启动时,Claude 第一动作必须是建 `project1/progress.md` + 对齐 Hand-write 规矩,**禁止**默认动手写任何配置文件。1.a 关闭。 |
| 2026-04-28       | 1.b    | ✅ `src/feedscope/cli.py` hand-written:`@app.command() def hello() -> None: typer.echo("Hello world!")` + `if __name__ == "__main__": app()`。Typer 3 件套(`Typer()` / `@app.command()` / `echo()`)Haichuan 自学完成。 |
| 2026-04-28       | —     | 🔧 **Python baseline 升 3.11 → 3.14**。Haichuan 装 `uv python install 3.14`(3.14.4),修改 `.python-version` + pyproject.toml 3 处(`requires-python` / `[tool.mypy] python_version` / `[tool.ruff] target-version`)。这 4 处 Hand-write 由 Haichuan 完成,Claude 给清单。 |
| 2026-04-28       | 1.c    | 🔧 **Build backend 切换 hatchling → uv_build**。Root cause:hatchling editable install 在路径含空格(`AI agent Engineer`)时,`_editable_impl_feedscope.pth` 内容指向 `src/` 正确,但 Python 不识别 → `import feedscope` 报 `ModuleNotFoundError`。Haichuan 改 pyproject.toml,把 `[build-system] requires = ["hatchling"]` + `[tool.hatch.build.targets.wheel]` 整段替换为 `requires = ["uv_build>=0.4.15"]` + `[tool.uv.build-backend] module-name = "feedscope" / module-root = "src"`。`rm -rf .venv uv.lock && uv sync` 后立即 work。**Lesson**:hatchling 在带空格路径有 editable bug;uv_build 是 uv 自家 backend,更宽容,且跟 uv 包管器一致。今后所有 project 默认用 uv_build。 |
| 2026-04-28       | 1.d    | 📘 **Typer single-command 行为**:`@app.command()` 只注册一个命令时 → typer 自动当 root command,`feedscope` 直接执行,`feedscope hello` 反而报 `Got unexpected extra argument (hello)`。Commit 6 加 `fetch` sub-command 后 typer 自动切换到 sub-command 模式,`feedscope hello` 自动恢复。 |
| 2026-04-28       | 1.d    | ✅ **三连验证全过**。`uv run feedscope` → "Hello world!" / `uv run mypy src/` → `Success: no issues found in 2 source files`(1 个无害 note `unused section(s): module = ['respx.*']`,Commit 3 用 respx 后消失)/ `uv run ruff check src/ tests/` → `All checks passed!`。 |
| 2026-04-28       | 1      | ✅ **Commit 1 关闭** — 1.b/c/d/e/f 全勾,git first commit 已打。Overall Progress **1/7**。下一步:Commit 2 Pydantic models — Hand-write 规矩 100% 严格执行,Claude 只 review 字段决策,不写代码。 |

*— end of file · 不要在这之后添加"下一步 checklist"。下一步只写在 Dashboard 的 `Next Action` 字段。*
