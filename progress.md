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
| **Current Commit**   | `Commit 7 — GitHub push + acceptance 自查(in progress · 收尾阶段)`                                                                                                                                                                                                                                                                                                                                                                                                            |
| **Overall Progress** | 🟩🟩🟩🟩🟩🟩🟦 6 / 7 commits done                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **Blocker**          | none                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **Last Activity**    | 2026-04-29 · **Commit 6 关闭** + ⭐ **path-with-space editable bug 彻底修复**。重写 cli.py(typer 2 commands:hello 占位 + fetch 真功能,4 options,asyncio.run 桥接,FetchConfig.model_validate 验 sources Literal,共享 httpx.AsyncClient),test_cli.py(2 个 CliRunner e2e tests),README 完整 12 个 section。**关键修复**:从 src-layout 切到 flat layout(`module-root = ""`)避开 path-space + .pth 间歇失效组合。**14 tests PASSED**(原 12 + 新 2)+ mypy clean + ruff clean + git commit 已打。 |
| **Working Mode**     | HAND-WRITE · resume-grade(Project 0 Commit 2+ 严格执行 — code 全部 Haichuan 写,Claude 只 review + 方向提示)|进度:完成驱动,非日历驱动                                                                                                                                                                                                                                                                                                                                |
| **Next Action**      | Commit 7 收尾 5 步:(1) 创建 GitHub public repo `feedscope`(GitHub UI 或 `gh repo create feedscope --public`);(2) `git remote add origin git@github.com:LovRanRan/feedscope.git`;(3) `git push -u origin main`;(4) 跑最后一次 acceptance 自查:14 tests / mypy / ruff / `feedscope --help` 都 work,确认 9 项 acceptance criteria 全 ✓;(5) 在 `final_checklist.md` 把 Project 0 的 acceptance checkbox 全勾掉 + 在 progress.md Logs 追加 "Project 0 完结" 行。 |

---

## 🗺️ Roadmap(7 commit · 按完成推进,不绑日期)

### Commit 1 — 项目脚手架 ✅ 2026-04-28

- [x] 1.a Hand-write 决策:选 **C**(Project 0 破例,Project 1+ 严格)✅ 2026-04-28
- [x] 1.b `src/feedscope/cli.py` Haichuan 自己写(typer 3 件套占位:`Typer()` + `@app.command() hello() -> None: typer.echo(...)` + `if __name__ == "__main__": app()`)✅ 2026-04-28
- [x] 1.c `uv sync` 装环境成功(经过 Python 3.14 升级 + build backend 切换 hatchling → uv_build)✅ 2026-04-28
- [x] 1.d 三连验证:`uv run feedscope` → "Hello world!" / `mypy --strict src/` Success / `ruff check` All passed ✅ 2026-04-28
- [x] 1.e `git init` + first commit(message: "Commit 1: project scaffolding (uv + ruff + mypy strict + typer entry, py3.14)")✅ 2026-04-28
- [x] 1.f Logs 追加完成行 + Dashboard 同步 ✅ 2026-04-28

### Commit 2 — Pydantic models ✅ 2026-04-29

- [x] 2.a `src/feedscope/models.py`:`Article`(title Annotated min_length=1 / url HttpUrl / source SourceName Literal / published_at AwareDatetime / authors list[str]|None / summary str="";frozen ConfigDict)✅ 2026-04-29
- [x] 2.b `FetchResult`(source SourceName / articles list[Article] default_factory list / fetched_at AwareDatetime default_factory `lambda: datetime.now(UTC)` / error str|None=None;frozen)✅ 2026-04-29
- [x] 2.c `src/feedscope/config.py`:`FetchConfig(BaseSettings)` — env_prefix=`FEEDSCOPE_` / env_file=`.env` / extra=`ignore`;query Annotated min_length=1 必填 / limit Field default=20 gt=0 le=100 / sources list[SourceName] default=`["arxiv","hn"]` / output_path Path|None=None ✅ 2026-04-29
- [x] 2.d 字段决策:`datetime`(秒级精度,unix int 自动转)/ `HttpUrl`(自动 normalize)/ `list[str]`(主流写法)/ `Literal["arxiv","hn"]` 抽成模块级 `SourceName` type alias 复用 ✅ 2026-04-29
- [x] 2.e `tests/test_models.py` 3 PASSED:`test_article_rejects_empty_title`(pytest.raises ValidationError)/ `test_article_parses_unix_timestamp`(1723737138 → 2024-08-15 15:52:18 UTC)/ `test_fetch_config_reads_env_var`(monkeypatch.setenv FEEDSCOPE_QUERY)✅ 2026-04-29
- [x] 2.f Commit message: "Commit 2: Pydantic models (Article, FetchResult, FetchConfig) + 3 validator tests" ✅ 2026-04-29

### Commit 3 — BaseFetcher + ArxivFetcher ✅ 2026-04-29

- [x] 3.a `src/feedscope/fetchers/__init__.py` 空 + `src/feedscope/fetchers/base.py`:`BaseFetcher(ABC)` `__init__(self, client: httpx.AsyncClient, timeout: float = 30.0)` + `@abstractmethod async def fetch(self, query: str, limit: int) -> FetchResult` ✅ 2026-04-29
- [x] 3.b 决策:**注入 httpx.AsyncClient**(test 友好 + orchestrator 共享 client 复用 connection)+ timeout 30s 默认 ✅ 2026-04-29
- [x] 3.c `src/feedscope/fetchers/arxiv.py`:`class ArxivFetcher(BaseFetcher)`,Atom XML namespace map `{"atom": "http://www.w3.org/2005/Atom"}`,httpx params dict 显式标 `dict[str, str | int]`(避免 mypy 推 `object`),3 类 except (HTTPStatusError / RequestError / ParseError) 都返回 FetchResult(error=...) 不抛 ✅ 2026-04-29
- [x] 3.d `tests/test_arxiv_fetcher.py` 3 PASSED:`returns_articles_on_success`(2 entries Atom XML)/ `handles_empty_results`(0 entries) / `returns_error_on_http_500`(error contains "HTTP 500" + Optional narrowing)。`@respx.mock` + `httpx.AsyncClient` ✅ 2026-04-29
- [x] 3.e Commit message: "Commit 3: BaseFetcher + ArxivFetcher with respx-mocked tests" ✅ 2026-04-29

### Commit 4 — HNFetcher + tests ✅ 2026-04-29

- [x] 4.a `src/feedscope/fetchers/hn.py`:`class HNFetcher(BaseFetcher)`,HN Algolia API endpoint + 3 query params (tags=story / query / hitsPerPage),JSON 解析,**url null fallback** (`hit.get("url")` + falsy check → `https://news.ycombinator.com/item?id={objectID}`),authors 包 `[hit["author"]]` list,summary=`""`,3 类 except (HTTPStatusError / RequestError / **JSONDecodeError** 替代 ParseError) ✅ 2026-04-29
- [x] 4.b `tests/test_hn_fetcher.py` 3 PASSED:`returns_articles_on_success`(3 hits 含 1 个 url null 测 fallback,验 `str(url) == thread URL`)/ `handles_empty_results` / `returns_error_on_http_500`。`HN_EMPTY_JSON: dict[str, Any]` 显式标注(空 list mypy 推不出元素类型) ✅ 2026-04-29
- [x] 4.c **里程碑达成**:BaseFetcher 现在有 ArxivFetcher + HNFetcher 2 个 sub-class,继承抽象 justified(面试讲"为什么用 abc"有依据,不是 over-engineering) ✅ 2026-04-29
- [x] 4.d Commit message: "Commit 4: HNFetcher (BaseFetcher now has 2 subclasses) + 3 respx-mocked tests" ✅ 2026-04-29

### Commit 5 — Orchestrator + JSON exporter ✅ 2026-04-29

- [x] 5.a `src/feedscope/orchestrator.py`:`FETCHERS: dict[SourceName, type[BaseFetcher]]` 注册表 + `async def run_fetchers(fetchers: Sequence[BaseFetcher], query, limit) -> list[FetchResult]` 用 `asyncio.gather(*[f.fetch(...) for f in fetchers], return_exceptions=True)` + `zip(strict=True)` 兜底 isinstance(BaseException) → FetchResult(source=fetcher.source, error=...) ✅ 2026-04-29
- [x] 5.b **Acceptance "asyncio for at least 1 concurrent operation" ✓** — `test_orchestrator_runs_fetchers_concurrently` 验 2 fetcher 各 sleep 0.1s 时 wall time < 0.15s(并发 ≈ 100ms vs 串行 200ms) ✅ 2026-04-29
- [x] 5.c `src/feedscope/exporter.py`:5 行核心 — `write_json(results, path)` 用 `r.model_dump(mode="json")` + `json.dumps(data, indent=2)` + `path.write_text(s, encoding="utf-8")` ✅ 2026-04-29
- [x] 5.d `tests/test_orchestrator.py` 3 PASSED:`runs_fetchers_concurrently`(timing) / `returns_all_results`(merge length) / `isolates_exceptions`(1 normal + 1 raise → 2 FetchResult,error contains "simulated fetcher bug")。FakeFetcher class 继承 BaseFetcher 但不调 super().__init__,实例 attrs:articles / delay / should_raise ✅ 2026-04-29
- [x] 5.e Scope creep:BaseFetcher 加 `source: ClassVar[SourceName]` + ArxivFetcher/HNFetcher 加 `source = "arxiv"`/`"hn"` + 所有 `source=` 字面值改 `source=self.source`(共 10 处 DRY) ✅ 2026-04-29
- [x] 5.f Commit message: "Commit 5: orchestrator (asyncio.gather) + JSON exporter" ✅ 2026-04-29

### Commit 6 — CLI 整合 + README ✅ 2026-04-29

- [x] 6.a `feedscope/cli.py` 重写:typer 2 commands(`hello` 占位 + `fetch` 主功能),`fetch` 4 options(query/sources/limit/output 各带 short flag),`asyncio.run(_run_fetch(config))` 桥接 sync→async,`FetchConfig.model_validate({...})` 验 sources Literal,`async with httpx.AsyncClient()` 共享给所有 fetcher ✅ 2026-04-29
- [x] 6.b CLI 决策:**sub-command** 路径(`feedscope fetch ...`),保留 hello 占位让 typer 启用 sub-command 模式(单 command 会降级 root mode) ✅ 2026-04-29
- [x] 6.c `tests/test_cli.py` 2 PASSED 用 `typer.testing.CliRunner`:`test_cli_help_lists_fetch_command` + `test_cli_fetch_help_shows_query_option`(验 typer 命令注册 + options 文档输出) ✅ 2026-04-29
- [x] 6.d ⭐ **path-with-space editable bug 彻底修复 — 转 flat layout**。`mv src/feedscope feedscope`,pyproject.toml `[tool.uv.build-backend] module-root = ""`,删 `mypy_path = ["src"]` + pytest `pythonpath = ["src"]`,mypy `files = ["feedscope", "tests"]`。`uv run feedscope --help` 终于稳定工作 ✅ 2026-04-29
- [x] 6.e `README.md` 完整 12 个 section:Status / Install / Usage(真 example + 输出 JSON 样本)/ CLI options 表 / Env vars / Architecture(ASCII 图 + 4 个 key components)/ Development / Test layout 表 / Acceptance criteria checklist / **Lessons learned 5 条第一人称** / Known limitations / License ✅ 2026-04-29
- [x] 6.f Commit message: "Commit 6: typer fetch command + test_cli + README + flat-layout fix" ✅ 2026-04-29

### Commit 7 — GitHub push + acceptance 自查 🟧 in progress

- [ ] 7.a `mypy --strict src/` 修所有报错(预计有 missing return type / Any / Optional handling)
- [ ] 7.b `ruff check src/ tests/` + `ruff format` 全清
- [ ] 7.c `pytest` 确认 ≥ 5 测试全过
- [ ] 7.d acceptance criteria 自查表:uv ✓ / 类继承 ✓(BaseFetcher → 2 子类) / mypy strict ✓ / asyncio 真并发 ✓ / Pydantic input+output ✓ / typer CLI ✓ / 5+ tests ✓ / README ✓ / public repo ≥ 5 commits ✓
- [ ] 7.e 创建 GitHub public repo(`feedscope`)+ `git remote add origin ...` + push
- [ ] 7.f Commit message: "Commit 7: mypy --strict clean + lint clean + verified acceptance"
- [ ] 7.g 在 `final_checklist.md` 把 Project 0 的 acceptance checkbox 全勾掉

---

## 📁 Repo 目录蓝图

`/Users/destiny/Desktop/AI_agent_Engineer/Final_checklist/Final_checklist_phase_projects/project0/` (2026-04-29 起;之前是 `AI agent Engineer/` 含空格,因 .pth 在含空格路径不稳定迁移)

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
| 2026-04-29       | 2.a    | ✅ **Article hand-written**(3 轮 review 收敛 🟢):第 1 轮 typo `authers/summery` + `source: str \| Literal[...]` union 等价于 str(Literal 失效)→ 🔴。第 2 轮 source 修了,加 `Annotated[str, Field(min_length=1)]` + `AwareDatetime` + `model_config = ConfigDict(frozen=True)`,提取 `SourceName = Literal["arxiv","hn"]` 模块级 type alias → 🟢。**Lesson**:`X | Literal[X-subset]` 在类型系统等价 `X`,Literal 失效;不要 union。 |
| 2026-04-29       | 2.b    | ✅ **FetchResult hand-written**(2 轮 review 🟢)。frozen 一致 + `articles: list[Article] = Field(default_factory=list)` + `fetched_at: AwareDatetime = Field(default_factory=lambda: datetime.now(UTC))`。**Bug catch**:第 1 轮写 `fetched_at = datetime.now(UTC)` 直接当 default(模块级求值,所有实例共享同一时间戳)→ default_factory lambda 修正。**Lesson**:任何 default 想"每次实例化都重新计算"必用 `default_factory=` 而非 `=`。 |
| 2026-04-29       | 2.c    | ✅ **FetchConfig hand-written**(3 轮 review 🟢)。1 轮 `from zipfile import Path`(VS Code auto-import 误推 zipfile.Path 而非 pathlib.Path)→ 🔴。2 轮 `class FetchConfig(BaseModel)` 没继承 BaseSettings(SettingsConfigDict 用了但 BaseModel 不读 env)→ 🔴。3 轮 `ge=0` allow `limit=0` → `gt=0` minor。**Lesson**:VS Code auto-import 在多个模块同名(Path)时常推错;Settings 类必须继承 BaseSettings,SettingsConfigDict 不让 BaseModel 自动读 env。 |
| 2026-04-29       | —     | 🔧 **mypy_path=["src"] + pydantic.mypy plugin 配置**。`tests/` 跑 mypy 时报 `Cannot find feedscope.models`(editable .pth mypy 不读)→ pyproject.toml `[tool.mypy] mypy_path = ["src"]`。后续 BaseSettings 报 `Argument missing for "query"`(BaseSettings 默认从 env 读但 mypy 不知道)→ 加 `plugins = ["pydantic.mypy"]`。Hand-write Haichuan 改。 |
| 2026-04-29       | —     | 🔧 **Build / install 折腾的最终方案:pytest pythonpath=["src"] 彻底绕过 editable install**。Commit 1 用过 hatchling 在路径含空格不稳 → 切 uv_build。Commit 2 中 editable .pth 文件内容正确(`/Users/.../project0/src`)但 Python 又不识别(原因不明,macOS + 路径空格组合)→ 在 `[tool.pytest.ini_options]` 加 `pythonpath = ["src"]`,pytest 启动时自己把 src/ 加到 sys.path,不依赖 .pth。**Lesson**:editable install 是脆弱组件;做 test 时用 pytest pythonpath / 跑业务代码用 entry point script,两条路并行最稳。 |
| 2026-04-29       | 2.e    | ✅ **3 tests PASSED hand-written**。全程 review 收敛包括:test 1 多余 type-ignore + 错指向 `from src.feedscope.config`(VS Code auto-import 误推 src. 前缀)→ 🔴 改成 `from feedscope.config`。test 2 写成 `pytest.raises` 测错方向(Pydantic 应该接受 unix int,不是抛错)→ 🟡 改成直接构造 + assert。**Lesson on unix timestamp**:1723737138 → 2024-08-15 **15:52:18** UTC(我之前给的 17:12:18 是错的,Pydantic 解析才对)。 |
| 2026-04-29       | 2.e    | 📘 **Lesson — Pylance ≠ mypy**。pydantic.mypy plugin 只对 mypy CLI 生效,Pylance/Pyright 不读。`FetchConfig()` 在 VS Code 仍红线 `reportCallIssue`,但 mypy 全过、pytest 全过、acceptance 不看 Pylance。**结论**:Pylance 红线是编辑器层提示,不等于真错误;以后看 mypy 终端输出为准,无视 Pylance 误报。如真需要消除红线,Phase 2 起加 `.vscode/settings.json` 关 `reportCallIssue`(单 project 级)。 |
| 2026-04-29       | 2      | ✅ **Commit 2 关闭** — 2.a/b/c/d/e/f 全勾。git commit "Commit 2: Pydantic models (Article, FetchResult, FetchConfig) + 3 validator tests" 已打。Overall Progress **2/7**。下一步:Commit 3 BaseFetcher abc + ArxivFetcher (Atom XML parsing) — Hand-write 100% 严格,Claude 只 review。 |
| 2026-04-29       | 3.a    | ✅ **BaseFetcher hand-written**(2 轮 review 🟢)。1 轮 `class base(ABC)` 类名小写违反 PEP 8 N801 → 🔴 改 `BaseFetcher`。包结构 `src/feedscope/fetchers/__init__.py`(空) + `base.py`。`__init__` 接 `client: httpx.AsyncClient` + `timeout: float = 30.0`,`@abstractmethod async def fetch(self, query, limit) -> FetchResult`。**Lesson**:Python 类名必须 PascalCase,小写 ruff `N801` 报错。 |
| 2026-04-29       | 3.c    | ✅ **ArxivFetcher hand-written**(3 轮 review 🟢)。1 轮 `@abstractmethod` 错放在 concrete 子类的 fetch 上 → 🔴(导致 ArxivFetcher 仍是 abstract,实例化 raise TypeError)+ 多余 `from abc import abstractmethod` import。2 轮 mypy 报 `params: dict[str, object]` 不兼容 httpx → 🔴 显式标 `dict[str, str | int]`。3 轮 `summary` 漏 `.strip()` 一致性 + `authors= authors` 等号空格。**关键 Lessons**:(1) `@abstractmethod` 只在抽象基类的方法上,concrete 子类提供实现时**不**带这个装饰器;(2) mypy strict 下 dict literal 混合类型推 `object`,要么显式标 union 要么避免混合。 |
| 2026-04-29       | 3.d    | ✅ **3 respx mock tests hand-written**(2 轮 review 🟢)。1 轮 vague placeholder `test_xxx` → 🟡 写真 3 个 test。2 轮 `import pytest` unused(test 没用 raises/monkeypatch/fixture) → 🔴 删。HTTP 500 test 用 `assert error is not None` 配合 `assert "HTTP 500" in error`,mypy 通过 Optional narrowing 知道第二行 error 是 str。**Lesson**:`@respx.mock` + `async def test_xxx()` + `async with httpx.AsyncClient() as client` 是 fetcher 异步测试的标准三件套。 |
| 2026-04-29       | —     | 📘 **Lesson — pydantic.mypy plugin 装上后,旧的 # type: ignore 反过来报 unused-ignore**。Commit 2 时为压制 Pylance/mypy 摩擦加过 ignore;装 plugin 后那个错本身消失,mypy strict 转而抱怨"unused"。**结论**:不要预防性加 ignore,plugin 装好后老 ignore 必须清理。 |
| 2026-04-29       | 3      | ✅ **Commit 3 关闭** — 3.a/b/c/d/e 全勾。**6 tests PASSED**(原 3 + 新 3)+ mypy clean + ruff clean + git commit 已打。Overall Progress **3/7**。下一步:Commit 4 HNFetcher — 结构跟 ArxivFetcher 镜像但更简单(JSON 不是 XML),关键里程碑是 BaseFetcher 终于有 2 个 sub-class,继承抽象 justified。 |
| 2026-04-29       | 4.a    | ✅ **HNFetcher hand-written**(2 轮 review 🟢)。1 轮 类名 `HnFetcher` 改 `HNFetcher`(PEP 8 acronym 全大写,跟 stdlib `HTTPClient` 一致)。结构跟 ArxivFetcher 镜像:同一个 `BaseFetcher` 父类、同样 `params: dict[str, str | int]` 类型注解模式、同样 try/except 3 类。差异点:(a) **url null fallback** — HN self-post 没外链,fallback 到 `https://news.ycombinator.com/item?id={objectID}`;(b) authors 单 string 包成 `list[str]`(HN 单 author);(c) summary 写死 `""`(HN 没此字段);(d) JSONDecodeError 替代 ParseError。**Lesson**:跨 fetcher 的差异都集中在"数据形态"(XML vs JSON / 多 author vs 单 author / 字段缺失策略),BaseFetcher 抽象层稳定不动 — 这正是 abc 的价值。 |
| 2026-04-29       | 4.b    | ✅ **3 respx mock tests hand-written**(2 轮 review 🟢)。1 轮 `assert result.source == "hb"` typo → 🔴(should "hn",pytest 会 fail);+ url assertion 写了两份重复(`unicode_string()` + `str(...)` 验同一件事)→ 🟡 删一个;+ 缺 `assert result.error is None` 在 success test 一致性 → 🟡 加上。2 轮 `HN_EMPTY_JSON = {"hits": []}` mypy 抱怨 `Need type annotation`(空 list 推不出元素类型)→ 🔴 加 `: dict[str, Any]` 显式标。**Lesson**:空 collection literal 在 mypy strict 下永远要显式标注,推不出元素类型。 |
| 2026-04-29       | 4.c    | 📘 **里程碑 — BaseFetcher 抽象 justified**。Commit 3 结束时只有 ArxivFetcher 一个 sub-class,abc 仿佛 over-engineering。Commit 4 HNFetcher 加上后,**两个 sub-class 共享相同接口**(`async fetch(query, limit) -> FetchResult`)+ **共享相同生命周期管理**(注入的 client + timeout)+ **共享错误契约**(3 类 except 不抛)。面试讲"为什么用 abc"答案有依据:接口契约 + DRY + Liskov substitution(orchestrator 收 list[BaseFetcher] 不关心具体子类)。 |
| 2026-04-29       | 4      | ✅ **Commit 4 关闭** — 4.a/b/c/d 全勾。**9 tests PASSED**(原 6 + 新 3)+ mypy clean + ruff clean + git commit 已打。Overall Progress **4/7**。下一步:Commit 5 Orchestrator(asyncio.gather 多源并发)+ JSON exporter(model_dump_json) — 这是 acceptance criteria "asyncio for at least 1 concurrent operation" 的核心证据。 |
| 2026-04-29       | 5.a    | ✅ **BaseFetcher source ClassVar + 跨 3 文件 DRY 重构 hand-written**(2 轮 review 🟢)。base.py 加 `source: ClassVar[SourceName]` 抽象属性(无 default,子类必须覆写);ArxivFetcher/HNFetcher 各加 `source = "arxiv"`/`"hn"` 类属性。1 轮 仅改了 Article 构造里的 source,FetchResult 4 处 `source="arxiv"` 漏改 → 🟡 改成 `source=self.source` 全覆盖,DRY 一致到底,2 个 fetcher 共 10 处。**Lesson**:DRY 要 commit 到底,半 DRY 比不 DRY 还混乱。 |
| 2026-04-29       | 5.b    | ✅ **orchestrator.py + exporter.py hand-written**(2 轮 review 🟢)。orchestrator 核心 `asyncio.gather(*[f.fetch(...)], return_exceptions=True)` + `zip(strict=True)` + `isinstance(BaseException)` 兜底转 FetchResult。FETCHERS 注册表 `dict[SourceName, type[BaseFetcher]]`。exporter 5 行:`r.model_dump(mode="json")` + `json.dumps(indent=2)` + `path.write_text(encoding="utf-8")`。 |
| 2026-04-29       | 5.d    | ✅ **test_orchestrator.py 3 PASSED hand-written**(2 轮 review 🟢)。FakeFetcher 继承 BaseFetcher 但跳过 super().__init__(test 不需要 client),实例 attrs `articles`/`delay`/`should_raise`。1 轮 placeholder `<some_article>` 没替换 → 🔴 改 `SAMPLE_ARTICLE`;`test_orchestrator_returns_all_results` 漏写 → 🔴 加上(2 fetcher × 2 articles → assert merge length 4)。 |
| 2026-04-29       | —     | 🔧 **Type 系统坑 — list invariance**。`run_fetchers(fetchers: list[BaseFetcher])` 拒绝 `list[FakeFetcher]`,因为 `list` 是 invariant(不变)。修法:**改 `Sequence[BaseFetcher]`**(`from collections.abc import Sequence`),Sequence 是只读 protocol → covariant(协变),子类 list 兼容父类 Sequence。**Lesson**:函数参数 default 用 Sequence/Iterable,内部确实需要 mutate 才用 list — Phase 2-3 写更多接口时一致 apply。 |
| 2026-04-29       | —     | 🔧 **Ruff `I001` import 排序 lesson**。`from collections.abc import Sequence` 误放在 `from feedscope.xxx` 后面,ruff 报排序错。Python import 标准 3 段:(1) 标准库;(2) 第三方;(3) 本地。每段空行分隔。`uv run ruff check --fix` 一键修。 |
| 2026-04-29       | 5      | ✅ **Commit 5 关闭** ⭐ — 5.a/b/c/d/e/f 全勾。**12 tests PASSED**(原 9 + 新 3)+ mypy 14 source files clean + ruff clean + git commit 已打。Overall Progress **5/7**。⭐ **关键里程碑达成 — Project 0 acceptance "asyncio for at least 1 concurrent operation" ✓ 满足**(orchestrator + 3 个 timing test 锁住)。下一步:Commit 6 CLI 整合 + README,把 typer 占位改成真 fetch 命令,把所有 building blocks 接到一起跑。 |
| 2026-04-29       | 6.a    | ✅ **cli.py 重写 hand-written**(3 轮 review 🟢)。typer 2 commands(`hello` 占位 + `fetch` 主功能),`fetch` 4 options(query/sources/limit/output),`asyncio.run(_run_fetch(config))` 桥接 sync→async,`FetchConfig.model_validate({...})` 验 sources Literal,`async with httpx.AsyncClient()` 一次创建共享给所有 fetcher,从 FETCHERS 注册表实例化 → run_fetchers → write_json。1 轮 ruff B008 `Path("out.json")` 嵌在 default → 改 string default。2 轮 ruff `extend-immutable-calls` 配置位置错(应在 `[tool.ruff.lint.flake8-bugbear]`)。 |
| 2026-04-29       | 6.a    | 🔧 **彻底修 path-with-space editable install bug — 转 flat layout**。Commit 1 起 src-layout(`src/feedscope/`)在 `/Users/.../AI agent Engineer/...` 路径下 .pth 间歇失效(Python site.py 可能某些条件不识别含空格 path,具体原因不明,但跨 hatchling/uv_build 重现)。**最终修法**:把 `src/feedscope/*` 移到 `feedscope/*`(flat layout),pyproject.toml 加 `[tool.uv.build-backend] module-root = ""`,删 `mypy_path = ["src"]` + pytest `pythonpath = ["src"]`,mypy `files = ["feedscope", "tests"]`。**Lesson** ⭐:**路径含空格 + src-layout + editable install 是脆弱组合,Phase 1+ 项目 default 用 flat layout** 或者把 project 移到无空格路径。flat layout 把 project root 加进 sys.path,无 .pth 中间层,跨 build backend 都稳。 |
| 2026-04-29       | 6.c    | ✅ **test_cli.py 2 PASSED hand-written**(2 轮 review 🟢)。用 `typer.testing.CliRunner` in-process 调用 typer app(快、可调试、不依赖 entry point script — 所以 test 不受 path-space editable bug 影响)。test 1 验 root `--help` 列出 hello + fetch;test 2 验 `fetch --help` 列出 --query / --sources / "Search keyword"。**Lesson**:CliRunner 比 subprocess 跑 CLI 快 50x+,且共享 test 进程的 mypy/ruff 上下文,首选。 |
| 2026-04-29       | 6.e    | ✅ **README.md hand-written + Lessons learned Claude 写**。12 个 section 全:Status / Install (LovRanRan/feedscope) / Usage 真 example + 输出 JSON 样本 / CLI options 表 / Env vars / Architecture ASCII 图 + 4 个 key components / Development / Test layout 表 / Acceptance checklist 9 项 / **Lessons learned 5 条第一人称(Haichuan 授权 Claude 直接写)** / Known limitations / License。 |
| 2026-04-29       | 6      | ✅ **Commit 6 关闭** — 6.a/b/c/d/e/f 全勾。**14 tests PASSED**(原 12 + 新 2)+ mypy 15 source files clean + ruff clean + git commit 已打。Overall Progress **6/7**。下一步:Commit 7 收尾 — GitHub repo 创建 + push + acceptance 9 项自查 + final_checklist.md 勾掉 Project 0 acceptance + progress.md 写 "Project 0 完结"。 |
| 2026-04-29       | —     | ⭐ **Path migration — `~/Desktop/AI agent Engineer/` → `~/Desktop/AI_agent_Engineer/`**(空格 → 下划线)。Commit 6 修复后(flat layout)entry point script 仍间歇 ModuleNotFoundError;flat layout 减少了 .pth 触发频率,但路径含空格本身仍是 .pth 不稳的根因。Haichuan 选择**根本性修复 — 把整个父目录从含空格改无空格**。一条 `mv "AI agent Engineer" "AI_agent_Engineer"` 解决,git 不受影响(git 跟绝对路径无关),`uv sync` + `uv run feedscope --help` 立即稳定工作。**Phase 1+ 永久受益**:所有未来 mini-project 都在 `AI_agent_Engineer/` 下,editable install 永远稳。**Lesson** ⭐:路径含空格 + Python `.pth` 机制是脆弱组合,根因修复永远比 workaround 长期成本低。**Memory 待 future session 自动同步**(本 session memory 写权限受限)。 |

*— end of file · 不要在这之后添加"下一步 checklist"。下一步只写在 Dashboard 的 `Next Action` 字段。*
