# 数据包架构来源 
https://github.com/XeKr-Dev/minecraft-pack-builder
数据包自动构建以便更好地维护和下载数据包

如果对本数据包有特殊的版本需要 可以在此链接自动构建需要的数据包内容 https://build.xekr.dev/#/halfkite/Reasonable-Crafting

# Reasonable Crafting 数据包介绍(介绍文本由AI生成)

> **Minecraft 数据包** | 作者：half_kite | 数据包版本0.8.0 | 适用版本：1.21-26.2        | 时间:2026-0706-2243 |

---

## 📦 总览 | Overview

**Reasonable Crafting** 是一个旨在优化原版合成逻辑的 Minecraft 数据包。核心思想是 **"合情合理的合成"**：让配方的产出比例更加合理、染色更加便捷、方块分解更加实用。所有配方均通过物品标签（item tags）实现，兼容性极佳。

**Reasonable Crafting** is a Minecraft datapack that optimizes vanilla crafting logic. Its core philosophy is **"reasonable recipes"**: more sensible input/output ratios, more convenient dyeing, and more practical block decomposition. All recipes use item tags for excellent compatibility.

---

## 🧱 楼梯合成优化 | Stair Recipes (`half_stairs`)

**改变**：原版 6 个木板 → 4 个楼梯，改为 6 个木板 → 6 个楼梯。

**Change**: Vanilla 6 planks → 4 stairs, now **6 planks → 6 stairs**.

**配方数量** | **Recipe count**：66 种楼梯（涵盖所有木材、石材、铜等）

```
6 × 木板/材料 → 6 × 对应楼梯
6 × planks/material → 6 × matching stairs
```

额外包含：蓝冰、浮冰、遮光玻璃的替代配方。

---

## 🎨 无序染色 | Shapeless Dyeing

蜡烛、玻璃、玻璃板、陶瓦、混凝土、混凝土粉末、羊毛、床 全部支持无序合成。

Candles, glass, glass panes, terracotta, concrete, concrete powder, wool, beds — all shapeless.

| 模式 | 配方 | 产出 |
|------|------|------|
| 单染 | 1 物品 + 1 染料 | 1 对应颜色物品 |
| 批量 | 8 物品 + 1 染料 | 8 对应颜色物品 |

| Mode | Recipe | Output |
|------|--------|--------|
| Single | 1 item + 1 dye | 1 dyed item |
| Bulk | 8 items + 1 dye | 8 dyed items |
  
 > 染料使用标签匹配，花朵、粉末等任意染料来源均可使用。
 > Dyes use tag matching — any dye source (flowers, powders, etc.) works.

 **配方数量** | **Recipe count**：16 色 × 对应模式

---

## 🗜️ 方块分解 | Block Decomposition (`data/half/recipe/craft/`)

**新增**：将方块分解回原材料，解决"合成太多无法回收"的问题。

**New**: Decompose blocks back into raw materials.

### 杂项分解 | Misc Decomposition（19 配方）

| 原料 → 产物 | 比例 |
|-------------|------|
| 羊毛 → 线 | 1 → 4 |
| 石英块 → 下界石英 | 1 → 4 |
| 砖块 → 红砖 | 1 → 4 |
| 下界砖块 → 下界砖 | 1 → 4 |
| 荧石 → 荧石粉 | 1 → 4 |
| 浮冰 → 冰 | 1 → 4 |
| 蓝冰 → 浮冰 | 1 → 9 |
| 西瓜 → 西瓜片 | 1 → 4 |
| 雪块 → 雪球 | 1 → 4 |
| 沙子 → 红沙 | 1 → 1 |
| 黏土 → 黏土球 | 1 → 4 |
| 烈焰粉 → 烈焰棒 | 2 → 1 |
| 紫水晶块 → 紫水晶碎片 | 1 → 4 |
| 海晶石 → 海晶碎片 | 1 → 4 |
| 海晶石砖 → 海晶碎片 | 1 → 4 |
| 滴水石块 → 尖滴石 | 1 → 4 |
| 下界疣块 → 下界疣 | 1 → 9 |
| 岩浆膏块 → 岩浆膏 | 1 → 4 |
| 红沙 → 沙子 | 1 → 1 |

### 切石分解 | Stonecutting Decomposition（8 配方）

使用切石机将方块分解为原材料，效率与手工分解相同。

### 简化合成 | Simplified Crafting（2 配方）

- 堆肥桶：`4 木板 → 2 堆肥桶`（原版为 7 木板 → 1）
- 遮光玻璃：`1 紫水晶块 + 1 任意玻璃 → 2 遮光玻璃`

---

## ⛏️ 原矿合成 | Ore Synthesis (`data/half/recipe/Ore/`)

**新增**：将原材料重新合成为矿石方块，让不可再生的矿石也能通过合成获得。支持多种原材料路径（粗矿、锭、块），浅层和深层矿石均可合成，同种矿石的配方在配方书中归为一组。

**New**: Craft ore blocks from raw materials, making non-renewable ores obtainable through crafting. Multiple material paths supported (raw ore, ingot, block), both stone and deepslate variants available. Recipes for the same ore type are grouped together in the recipe book.

### 矿石合成 | Ore Crafting（30 配方）

| 产物 Ore | 配方路径 | 图案 Pattern |
|----------|----------|:---:|
| 煤矿石 Coal Ore | 煤 ×4 + 石头/深板岩 ×4 | 十字 |
| 铁矿石 Iron Ore | 粗铁/铁锭 ×4 + 石头/深板岩 ×4 | 十字 |
| 金矿石 Gold Ore | 粗金/金锭 ×4 + 石头/深板岩 ×4 | 十字 |
| 铜矿石 Copper Ore | 粗铜×2 + 粗铜块×2 + 石头/深板岩（锭版：铜锭+铜块） | 对角十字 |
| 钻石矿石 Diamond Ore | 钻石 ×4 + 石头/深板岩 ×4 | 十字 |
| 绿宝石矿石 Emerald Ore | 绿宝石 ×4 + 石头/深板岩 ×4 | 十字 |
| 青金石矿石 Lapis Ore | 青金石块 + 石头/深板岩 ×4 | 十字 |
| 红石矿石 Redstone Ore | 红石粉 ×8 + 石头/深板岩（包围） | 环状 |
| 下界石英矿石 Nether Quartz | 下界石英 ×4 + 下界岩 ×4 | 十字 |
| 下界金矿石 Nether Gold Ore | 金粒×6 + 金锭×2 + 下界岩 | 满格 |
| 粗铁/粗金/粗铜 | 锭 + 石头/深板岩 → 对应粗矿 |
| 粗铁块/粗金块/粗铜块 | 块 + 石头/深板岩 ×4 → 对应粗矿块 |

**配方数量** | **Recipe count**：30

---

## 🔥 烧炼回收 | Smelting Recovery (`data/half/recipe/scrap/`)

**新增**：烧炼粗矿块可直接获得对应的块（熔炉、高炉都可以），以及混凝土粉末烧成染色玻璃。

**新**: Smelt raw ore blocks directly into metal blocks, 和 concrete powder into stained glass.

| 原料 | 产物 | 经验 |
|------|------|------|
| 粗铁块 → 铁块 | 6.3 XP |
| 粗铜块 → 铜块 | 6.3 XP |
| 粗金块 → 金块 | 6.3 XP |
| 16 色混凝土粉末 → 对应染色玻璃 | 0.1 XP × 16 |

**配方数量** | **Recipe count**：19

---

## 📊 统计汇总 | Summary

| 模块 Module | 配方数 Recipes | 类型 Type |
|-------------|:-----------:|------|
| 楼梯 Stairs | 58 | 有序 → 更高效 |
| 蜡烛 Candle | 32 | 无序染色 |
| 玻璃 Glass | 64 | 无序染色 |
| 羊毛 Wool | 32 | 无序染色 |
| 地毯 Carpet | 32 | 无序染色 |
| 床 Bed | 16 | 无序染色 |
| 染料 Dye | 12 | 扩展混合 |
| 陶瓦 Terracotta | 32 | 无序染色 |
| 混凝土转换 Concrete | 32 | 无序转换 |
| 杂项分解 Misc | 19 | 分解回收 |
| 切石分解 Stonecutting | 8 | 切石回收 |
| 原矿合成 Ore Synthesis | 30 | 合成矿石 |
| 烧炼回收 Scrap | 19 | 烧炼回收 |
| 简化合成 Simplify | 2 | 简化优化 |
| **总计 Total** | **388** | |
