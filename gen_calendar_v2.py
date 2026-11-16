#!/usr/bin/env python3
"""生成《方案A 每日执行日历 v2：含地点与 AI/Skill 分配》。"""
from datetime import date, timedelta

START = date(2026, 11, 9)  # 周一
WD = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
SLOTS = {
    0: "20:30–23:00（2.5h）", 1: "20:30–23:00（2.5h）", 2: "休息",
    3: "20:30–23:00（2.5h）", 4: "20:30–23:00（2.5h）",
    5: "09:30–12:00 / 14:00–17:30（6h）",
    6: "09:30–12:00 / 14:00–16:30（5h，含 30min 复盘）",
}

# (周, 主题, 本周验收, [(地点, AI, Skill, 任务) x6])  顺序：一二四五六日
D = "DSH"; Q = "Qoder"; W = "WorkBuddy"; M = "Meoo"; C = "CloudBase"
DESK = "🖥 书桌"; LAP = "💻 笔记本"; PHONE = "📱 手机"

WEEKS = [
(1, "装环境 + 跑通移动", "能跑能跳、相机不穿墙", [
 (DESK, Q, "godot-scene-arch", "装 Godot 4.7.2 / Blender / Blockbench / Git；用 Qoder 定工程目录与编码约定"),
 (DESK, D, "godot-gdscript", "建空工程，开严格类型，配输入映射"),
 (DESK, D, "godot-gdscript", "角色场景：CharacterBody3D + 胶囊碰撞"),
 (DESK, D, "godot-gdscript", "相机：第三人称跟随 + 鼠标视角 + 遮挡收缩"),
 (DESK, D, "playtest-report", "灰盒场景跑动测试，记 5 条手感问题"),
 (LAP, W, "playtest-report", "录 10 秒移动视频，建 Git 仓库并首次提交"),
]),
(2, "交互与存档骨架", "能开门坐下、存档不丢", [
 (DESK, D, "godot-gdscript", "交互基类：射线检测 + 提示 UI"),
 (DESK, D, "godot-gdscript", "门与椅子：可开、可坐"),
 (LAP, Q, "godot-scene-arch", "评审交互与存档设计，找出 3 个上联机会爆炸的点"),
 (DESK, D, "godot-gdscript", "存档骨架：GameState + Save 单例"),
 (DESK, D, "godot-gdscript", "存档读回：退出再进位置不变"),
 (LAP, W, "playtest-report", "自测 + 写 5 条已知问题，整理成 issue 清单"),
]),
(3, "教学楼 1 层建模（模块化）", "1 层白模可走、面数 <8k", [
 (DESK, Q, "lowpoly-asset", "定模块尺寸与命名规范，写导入脚本骨架"),
 (DESK, D, "blockbench-model", "做墙、窗、门三个模块"),
 (DESK, D, "blockbench-model", "做楼梯与护栏模块，导入 Godot"),
 (DESK, D, "lowpoly-asset", "按平面图拼出走廊与两间教室"),
 (DESK, D, "lowpoly-asset", "补走廊灯与天花，检查穿模"),
 (LAP, D, "playtest-report", "走查 10 分钟，记下不合理处并修 3 处"),
]),
(4, "教室家具与氛围", "一间完整教室、24 桌不卡", [
 (DESK, Q, "godot-scene-arch", "联机架构选型：ENet 直连 vs 中继，出选型文档"),
 (DESK, D, "blockbench-model", "课桌：桌面 + 桌腿 + 抽屉，300 tri 内"),
 (DESK, D, "blockbench-model", "椅子 + 黑板 + 讲台 + 时钟"),
 (DESK, D, "lowpoly-asset", "用 MultiMesh 摆 24 套桌椅，测帧率"),
 (DESK, D, "lowpoly-asset", "灯光：日光 + 走廊冷白，调曝光"),
 (LAP, W, "playtest-report", "验收 + 截图，把选型文档做成 1 页 PPT 存档"),
]),
(5, "上课玩法", "能完整走完一堂课", [
 (DESK, D, "godot-gdscript", "设计上课流程：打铃→点名→记笔记→下课"),
 (DESK, D, "godot-gdscript", "打铃：定时器 + 音效占位 + 全体 NPC 入座"),
 (DESK, D, "godot-gdscript", "点名：随机点到玩家，按键应答"),
 (DESK, D, "godot-gdscript", "传纸条：扔纸团 + 抛物线与落点判定"),
 (DESK, D, "playtest-report", "把三个交互串成 3 分钟完整课堂"),
 (LAP, W, "playtest-report", "试玩两遍修断点，写 v0.1 测试问卷"),
]),
(6, "收口与第一次外部测试", "v0.1 发出去", [
 (DESK, D, "playtest-report", "修上周遗留 bug"),
 (DESK, D, "lowpoly-asset", "补教室细节：粉笔槽、课程表、海报"),
 (LAP, M, "release-checklist", "用秒悟做官网 v0：介绍 + 3 张截图 + 下载占位"),
 (DESK, D, "godot-gdscript", "音效占位：脚步、铃、椅子摩擦"),
 (LAP, W, "release-checklist", "录 30 秒宣传片段 + 写试玩说明"),
 (LAP, D, "scope-guard", "发给 2 个朋友试玩，整理反馈，定 v0.1 问题清单"),
]),
(7, "联机骨架", "两人能同场景看见彼此", [
 (DESK, C, "net-debug", "CloudBase 建免费环境，跑通云函数 hello"),
 (DESK, D, "net-debug", "ENet 创建主机 / 加入，跑通握手"),
 (DESK, D, "net-debug", "房间码：IP+端口 Base64，复制粘贴加入"),
 (DESK, D, "net-debug", "双人进同一场景，验证位置同步"),
 (DESK, D, "net-debug", "修同步抖动，加插值"),
 (LAP, W, "playtest-report", "4 人同时进，记录问题并排序"),
]),
(8, "动画与交互同步", "4 人 30 分钟不崩", [
 (DESK, D, "net-debug", "同步动画状态：走/跑/坐/挥手"),
 (DESK, D, "net-debug", "同步交互：开门、坐下、上课状态"),
 (DESK, D, "net-debug", "延迟测试：人为 150ms，观察表现"),
 (DESK, D, "net-debug", "修抖动与瞬移，加客户端预测"),
 (DESK, W, "net-debug", "把 4 人压力测试日志丢给 WorkBuddy 分析"),
 (LAP, D, "playtest-report", "写联机已知问题清单"),
]),
(9, "断线与稳定性", "拔网线能重连不崩", [
 (DESK, D, "net-debug", "断线重连：保留角色 30 秒"),
 (DESK, D, "net-debug", "超时移除与状态清理"),
 (DESK, D, "net-debug", "重连后状态恢复（位置/任务/血量）"),
 (DESK, D, "playtest-report", "反复拔网线测试 10 次"),
 (DESK, D, "net-debug", "修 bug，补日志"),
 (LAP, D, "scope-guard", "联机阶段小结，判断是否触发止损降级"),
]),
(10, "食堂", "食堂可进、可打饭", [
 (DESK, D, "lowpoly-asset", "画食堂平面：窗口、餐桌区、后厨门"),
 (DESK, D, "blockbench-model", "建模打饭窗口与餐台"),
 (DESK, D, "blockbench-model", "餐桌椅（复用教室椅子改色）"),
 (DESK, D, "godot-gdscript", "打饭交互：排队、选菜、端走"),
 (DESK, D, "lowpoly-asset", "后厨门与灯光，接入主场景"),
 (LAP, W, "playtest-report", "走查 + 验收，更新资产清单"),
]),
(11, "宿舍", "宿舍外观 + 样板房", [
 (DESK, D, "lowpoly-asset", "宿舍楼外观建模（窗格 + 阳台）"),
 (DESK, D, "blockbench-model", "样板房：床、书桌、衣柜"),
 (DESK, D, "godot-gdscript", "门禁交互：白天可进，夜里锁门"),
 (DESK, D, "lowpoly-asset", "接入主场景，调整地形贴合"),
 (DESK, D, "playtest-report", "走查 + 修穿模"),
 (LAP, D, "playtest-report", "验收 + 截图存档"),
]),
(12, "室外与止损评估", "校园轮廓完整、45fps", [
 (DESK, D, "lowpoly-asset", "地形：草地起伏 + 石板路"),
 (DESK, D, "godot-gdscript", "湖面：水面 shader + 岸边碰撞"),
 (DESK, D, "lowpoly-asset", "围墙与校门，限制活动范围"),
 (DESK, D, "lowpoly-asset", "树与草丛（素材包 + 改色）"),
 (DESK, D, "godot-gdscript", "性能优化：合批、LOD、阴影距离"),
 (LAP, D, "scope-guard", "联机复测，决定是否降到 2 人"),
]),
(13, "教学楼补齐 3 层", "三层走通不迷路", [
 (DESK, D, "lowpoly-asset", "2 层：两间教室（换色换装饰）"),
 (DESK, D, "blockbench-model", "3 层：办公室（办公桌、文件柜）"),
 (DESK, D, "lowpoly-asset", "厕所与楼梯间"),
 (DESK, D, "playtest-report", "整体走查：动线、标识、灯光一致性"),
 (DESK, D, "playtest-report", "修 5 处穿模与 3 处卡点"),
 (LAP, D, "playtest-report", "验收 3 层可完整走通"),
]),
(14, "整合与 v0.2", "v0.2 联机版，4 人可玩", [
 (DESK, D, "playtest-report", "全场景整合测试（单人 + 联机）"),
 (DESK, D, "net-debug", "整理 bug 清单，按严重度排序"),
 (LAP, M, "dialogue-json", "用秒悟做任务/对话 JSON 网页编辑器"),
 (DESK, D, "net-debug", "修前 20 个 bug"),
 (DESK, D, "playtest-report", "联机 + 场景复测"),
 (LAP, W, "release-checklist", "录 1 分钟 v0.2 演示，发测试玩家"),
]),
(15, "对话系统", "改 JSON 不改代码", [
 (DESK, D, "dialogue-json", "定对话 schema：节点/分支/条件/变量"),
 (DESK, D, "dialogue-json", "实现对话播放器与选项 UI"),
 (DESK, D, "godot-gdscript", "条件与变量：任务状态、好感、时间"),
 (DESK, D, "dialogue-json", "做调试面板，能跳节点"),
 (DESK, D, "dialogue-json", "写 2 段示例对话并联调"),
 (LAP, D, "playtest-report", "验收：改 JSON 不改代码"),
]),
(16, "任务系统", "三条支线骨架可通", [
 (DESK, D, "dialogue-json", "定任务 schema：接取/目标/奖励/失败"),
 (DESK, D, "godot-gdscript", "接取与追踪 UI"),
 (DESK, D, "godot-gdscript", "完成判定与奖励发放"),
 (DESK, D, "narrative-branch", "3 条支线骨架接入（占位文本）"),
 (DESK, D, "narrative-branch", "联机下任务状态同步"),
 (LAP, D, "playtest-report", "验收：能接、能做、能交"),
]),
(17, "陀螺对决", "陀螺 30 秒一局", [
 (DESK, D, "godot-gdscript", "定规则：蓄力、3 次碰撞、属性克制"),
 (DESK, D, "lowpoly-asset", "陀螺模型与旋转动画"),
 (DESK, D, "godot-gdscript", "蓄力条与碰撞判定"),
 (DESK, D, "godot-gdscript", "数值与平衡（3 局两胜）"),
 (DESK, D, "godot-gdscript", "小游戏入口与结算 UI"),
 (LAP, D, "playtest-report", "验收：30 秒能打完一局"),
]),
(18, "橡皮大战", "橡皮连打 10 局不出错", [
 (DESK, D, "godot-gdscript", "定规则：回合制、角度 + 力度、掩体"),
 (DESK, D, "lowpoly-asset", "橡皮与桌面场景"),
 (DESK, D, "godot-gdscript", "弹道与碰撞、回合切换"),
 (DESK, D, "godot-gdscript", "掩体与道具（橡皮擦、尺子）"),
 (DESK, D, "godot-gdscript", "结算与奖励"),
 (LAP, D, "playtest-report", "验收：连打 10 局"),
]),
(19, "NPC 资产与日程", "NPC 按作息走动", [
 (DESK, D, "lowpoly-asset", "NPC 形象 1–3：建模 + 贴图 + 骨骼绑定"),
 (DESK, D, "blockbench-model", "NPC 形象 4–6：换装复用"),
 (DESK, D, "godot-gdscript", "日程表数据：每个 NPC 的时间-地点"),
 (DESK, D, "godot-gdscript", "寻路：NavigationRegion3D + 简单避让"),
 (DESK, D, "playtest-report", "联调：NPC 到点换位置"),
 (LAP, D, "playtest-report", "验收：NPC 按时间出现在正确地点"),
]),
(20, "LLM 闲聊", "能聊、断网有兜底", [
 (DESK, C, "godot-gdscript", "CloudBase 云函数部署 LLM 代理（持 key、限流、日志）"),
 (DESK, D, "narrative-branch", "人设卡：每个 NPC 的语气、禁忌、知识范围"),
 (DESK, D, "godot-gdscript", "敏感词过滤 + 兜底台词"),
 (DESK, D, "godot-gdscript", "Godot 侧接入：请求、超时、降级"),
 (DESK, D, "net-debug", "断网测试：必须回落到本地台词"),
 (LAP, W, "playtest-report", "压测 50 次对话，算成本与延迟"),
]),
(21, "UI 全套", "启动到进游戏无断点", [
 (DESK, D, "godot-gdscript", "主菜单：开始、加入房间、设置、退出"),
 (DESK, D, "godot-gdscript", "房间界面：建/进、房间码、玩家列表"),
 (DESK, D, "godot-gdscript", "HUD：血量、任务追踪、交互提示"),
 (DESK, D, "godot-gdscript", "设置：音量、画质、按键、语言"),
 (DESK, D, "godot-gdscript", "任务面板与背包"),
 (LAP, D, "playtest-report", "全流程走查，修错位"),
]),
(22, "内容填充", "三条支线可通关", [
 (DESK, D, "narrative-branch", "支线 1「湖底的回声」全文 + 触发条件"),
 (DESK, D, "narrative-branch", "支线 2「办公室的抽屉」全文"),
 (LAP, M, "narrative-branch", "用秒悟做社区页（公告 + 反馈 + 作品墙）"),
 (DESK, D, "dialogue-json", "支线 3「会议室的那盏灯」全文"),
 (DESK, D, "scope-guard", "奖励表与道具表落地，死路检查"),
 (LAP, D, "playtest-report", "试玩三条线，修逻辑"),
]),
(23, "外部测试", "20 条问题已排序", [
 (DESK, D, "playtest-report", "全流程自测，记录卡点"),
 (DESK, D, "playtest-report", "找 3 个真人试玩（不是朋友也行）"),
 (DESK, D, "playtest-report", "收集问题，录入清单"),
 (DESK, D, "playtest-report", "按严重度分类：崩溃/卡死/体验/文案"),
 (LAP, W, "scope-guard", "把测试记录整理成报告，排优先级"),
 (LAP, D, "playtest-report", "修 10 个高危问题"),
]),
(24, "砍与修", "崩溃清零", [
 (DESK, D, "playtest-report", "修 bug 第二批"),
 (DESK, D, "scope-guard", "砍掉做不完的 20%（按砍单顺序）"),
 (DESK, D, "playtest-report", "回归测试：联机、存档、任务"),
 (DESK, D, "godot-gdscript", "性能优化：目标机型 45fps"),
 (DESK, D, "release-checklist", "存档兼容性检查"),
 (LAP, W, "release-checklist", "验收稳定版，写发布检查表"),
]),
(25, "打磨", "可发布候选版", [
 (DESK, D, "release-checklist", "音频：环境音、铃、食堂嘈杂、BGM"),
 (DESK, D, "godot-gdscript", "UI 动效与过渡"),
 (LAP, M, "release-checklist", "用秒悟做下载页 + 更新日志页"),
 (DESK, D, "godot-gdscript", "氛围细节：公告栏、涂鸦、天气"),
 (DESK, D, "release-checklist", "打包导出，目标机型实测"),
 (LAP, D, "release-checklist", "修最后一轮问题，定发布候选版"),
]),
(26, "发布", "v1.0 上线", [
 (LAP, M, "release-checklist", "itch.io 页面：简介、标签、配置要求"),
 (DESK, D, "release-checklist", "截图 4 张 + 30 秒预告片"),
 (DESK, C, "release-checklist", "上传构建，CloudBase 托管官网并写更新说明"),
 (DESK, D, "release-checklist", "发布 + 发群 + 发社区"),
 (DESK, W, "playtest-report", "盯首日反馈，修紧急 bug"),
 (LAP, D, "scope-guard", "项目复盘：工时、偏差、下一步"),
]),
]

out = []
out.append("# 方案 A · 每日任务表 v2（含地点与 AI/Skill）\n")
out.append("""> 起始 2026-11-09，结束 2027-05-09　｜　21h/周 × 26 周 ≈ 546 小时
> 配套：`方案A_垂直切片优先.md`、`资源与额度使用计划.md`、`skills/技能清单与模板.md`

## 地点 = 场景 + 设备

| 标记 | 场景 | 能做什么 | 不能做什么 |
|---|---|---|---|
| 🖥 书桌 | 书房/卧室，装 Godot + Blender 的主机 | 建模、联机调试、性能测试、打包 | 长时间建模容易腰疼，每 50 分钟起身 |
| 💻 笔记本 | 沙发、床上、图书馆、咖啡馆 | 写文档、改 JSON、评审、生成网页、整理反馈 | 跑不动 Blender 大场景，别在这做建模 |
| 📱 手机 | 通勤、排队、睡前 | 看参考、听音效、记点子、回消息 | 不产生交付物，不计工时 |

## AI 分工（按你手上的额度）

| AI | 什么时候用 | 剩余额度 | 到期 |
|---|---|---|---|
| **DSH**（主力） | 90% 的写码、调试、文档 | 按量 | 无 |
| **Qoder** | 只做评审、架构选型、规范生成 | 1 个月 | **2026-12-04** |
| **WorkBuddy** | 文档、PPT、日志分析、反馈整理 | 3000 积分（当月清零） | 每月 1 日重置 |
| **Meoo** | 官网、下载页、社区页、JSON 编辑器 | 50000 积分 | 待确认 |
| **CloudBase** | LLM 代理、账号/排行榜、静态托管 | 3000 资源点/月 | 约 2027-05 |

## 技能（Skill）一览

`godot-gdscript` 写脚本规范　`godot-scene-arch` 场景与架构　`lowpoly-asset` 低模规范　`blockbench-model` 建模步骤
`dialogue-json` 对话数据　`narrative-branch` 剧情结构　`net-debug` 联机排查　`playtest-report` 测试整理
`scope-guard` 砍需求　`release-checklist` 发布检查

> Skill 是提示词包，不会替你编译。默认在 DSH 里点名调用；标了 Qoder / WorkBuddy / Meoo 的天，把同一份 SKILL.md 贴进去即可。

---

""")

for w, theme, check, days in WEEKS:
    monday = START + timedelta(weeks=w - 1)
    out.append(f"## 第 {w} 周 · {theme}\n")
    out.append(f"`{monday.isoformat()} → {(monday + timedelta(days=6)).isoformat()}`　本周验收：**{check}**\n")
    out.append("| 日期 | 星期 | 时间 | 地点 | 任务 | AI · Skill |")
    out.append("|---|---|---|---|---|---|")
    ti = 0
    for d in range(7):
        day = monday + timedelta(days=d)
        if d == 2:
            out.append(f"| {day.isoformat()} | 周三 | 休息 | — | 不碰项目（可在手机上看参考，不算工时） | — |")
            continue
        loc, ai, sk, task = days[ti]
        ti += 1
        out.append(f"| {day.isoformat()} | {WD[d]} | {SLOTS[d]} | {loc} | {task} | **{ai}** · `{sk}` |")
    out.append("")

out.append("""---

## 里程碑

| 里程碑 | 截止 | 硬指标 | 不达标 |
|---|---|---|---|
| M1 可走可看 | 2026-12-20（W6） | 教室可玩、v0.1 发出 | 建模拖期 → 改用素材包 |
| M2 能联机 | 2027-02-14（W14） | 4 人同屏 30 分钟不崩 | 降到 2 人，省 20h 补小游戏 |
| M3 有内容 | 2027-04-11（W22） | 2 小游戏 + 3 支线可通 | 砍第 3 条支线 |
| M4 发布 | 2027-05-09（W26） | DoD 全绿 | 延期不超过 2 周 |

## AI 额度时间线

| 日期 | 事件 | 动作 |
|---|---|---|
| 2026-11-09 → 12-04 | Qoder 有效期 | 把架构、评审、选型做完，12/1 前导出到 `docs/` |
| 每月 1 日 | WorkBuddy 积分重置 | 月初列出本月要它做的 5 件事，当月用完 |
| 2027-04-01 | CloudBase 到期前 1 个月 | 决定续费（19.9 元/月）还是迁回本地 |
| 不定 | Meoo 积分有效期 | 登录控制台确认，有期限就提前用 |

## 每周固定动作

- 周一开工前 5 分钟：`git pull` → 看本周验收 → 写下「今天做完什么算完成」
- 每天收工 5 分钟：`git commit -m "W{n}-{日}: 做了什么"`
- 周日最后 30 分钟：更新 `progress.md`（做完什么 / 卡在哪 / 下周砍什么）
- 每周三：不碰项目
""")

open("执行日历_方案A_v2.md", "w", encoding="utf-8").write("\n".join(out))
print("ok")
