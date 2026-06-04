# Reasonable Crafting 数据包介绍

> **Minecraft 数据包** | 作者：half_kite | 适用版本：1.21+

---

## 📦 总览 | Overview

**Reasonable Crafting** 是一个旨在优化原版合成逻辑的 Minecraft 数据包。核心思想是 **"合情合理的合成"**：让配方的产出比例更加合理、染色更加便捷、方块分解更加实用。所有配方均通过物品标签（item tags）实现，兼容性极佳。

**Reasonable Crafting** is a Minecraft datapack that optimizes vanilla crafting logic. Its core philosophy is **"reasonable recipes"**: more sensible input/output ratios, more convenient dyeing, and more practical block decomposition. All recipes use item tags for excellent compatibility.

---

## 🧱 楼梯合成优化 | Stair Recipes (`half_stairs`)

**改变**：原版 6 个木板 → 4 个楼梯，改为 **3 个木板 → 6 个楼梯**，产出翻倍。

**Change**: Vanilla 6 planks → 4 stairs, now **3 planks → 6 stairs**, doubling the yield.

**配方数量** | **Recipe count**：58 种楼梯（涵盖所有木材、石材、铜等）

```
3 × 木板/材料 → 6 × 对应楼梯
3 × planks/material → 6 × matching stairs
```

额外包含：蓝冰、浮冰、遮光玻璃的替代配方。

---

## 🕯️ 蜡烛染色 | Candle Dyeing (`half_candle`)

**新增**：直接用染料给蜡烛染色，无需工作台摆图案。

单染：`1 蜡烛 + 1 染料 → 1 染色蜡烛`（16 色 × 1）
批量：`8 蜡烛 + 1 染料 → 8 染色蜡烛`（16 色 × 1）

**New**: Dye candles directly without crafting table patterns.

Single: `1 candle + 1 dye → 1 dyed candle` (16 colors)
Bulk: `8 candles + 1 dye → 8 dyed candles` (16 colors)

**配方数量** | **Recipe count**：32

---

## 🪟 玻璃染色 | Glass Dyeing (`half_glass`)

**改变**：原版只能在固定位置摆放玻璃+染料，现在改为无序合成，且支持单染和批量两种模式。

**Change**: Vanilla requires placing glass + dye in fixed positions. Now shapeless, supporting both single and bulk dyeing.

| 模式 | 配方 | 产出 |
|------|------|------|
| 批量染色玻璃 | 8 玻璃方块 + 1 染料 | 8 染色玻璃 |
| 单染玻璃 | 1 玻璃方块 + 1 染料 | 1 染色玻璃 |
| 批量染色玻璃板 | 8 玻璃板 + 1 染料 | 8 染色玻璃板 |
| 单染玻璃板 | 1 玻璃板 + 1 染料 | 1 染色玻璃板 |

**配方数量** | **Recipe count**：64（16 色 × 4 种模式）

---

## 🧶 羊毛染色 | Wool Dyeing (`half_wool`)

**新增**：直接用染料给羊毛染色（原版只有白色羊毛可染）。

单染：`1 羊毛 + 1 染料 → 1 染色羊毛`
批量：`8 羊毛 + 1 染料 → 8 染色羊毛`

**New**: Direct wool dyeing (vanilla only allows white wool dyeing).

Single: `1 wool + 1 dye → 1 dyed wool`
Bulk: `8 wool + 1 dye → 8 dyed wool`

**配方数量** | **Recipe count**：32（16 色 × 2 种模式）

---

## 🏠 地毯染色 | Carpet Dyeing (`half_carpet`)

**新增**：直接用染料给地毯染色。

单染：`1 地毯 + 1 染料 → 1 染色地毯`
批量：`8 地毯 + 1 染料 → 8 染色地毯`

**New**: Direct carpet dyeing with dyes.

Single: `1 carpet + 1 dye → 1 dyed carpet`
Bulk: `8 carpets + 1 dye → 8 dyed carpets`

**配方数量** | **Recipe count**：32（16 色 × 2 种模式）

---

## 🛏️ 床染色 | Bed Dyeing (`half_bed`)

**新增**：直接用染料给床染色（原版只能用同色羊毛合成床）。

`1 床 + 1 染料 → 1 染色床`

**New**: Direct bed dyeing (vanilla only allows crafting beds with matching wool color).

`1 bed + 1 dye → 1 dyed bed`

**配方数量** | **Recipe count**：16（16 色）

---

## 🎨 染料合成 | Dye Crafting (`half_dye`)

**增强**：扩展了可混合合成的染料种类，使用标签匹配任意形式的染料来源（花、粉末等均可）。

**Enhanced**: Extended dye mixing recipes using tags to match any dye source (flowers, powders, etc.).

| 配方 | 原料 | 产出 |
|------|------|------|
| 青色染料 Cyan | 蓝 + 绿 | 2 |
| 灰色染料 Gray | 黑 + 白 | 2 |
| 淡蓝染料 Light Blue | 蓝 + 白 | 2 |
| 淡灰染料 Light Gray | 黑 + 白 或 灰 + 白 | 2 × 2 |
| 黄绿染料 Lime | 绿 + 白 | 2 |
| 品红染料 Magenta | 蓝+红+白 / 蓝+红+粉 / 紫+粉 | 3 / 3 / 2 |
| 橙色染料 Orange | 红 + 黄 | 2 |
| 粉红染料 Pink | 红 + 白 | 2 |
| 紫色染料 Purple | 蓝 + 红 | 2 |

**配方数量** | **Recipe count**：12

---

## 🟫 陶瓦染色 | Terracotta Dyeing (`half_terracotta`)

**改变**：原版必须按固定图案摆放陶瓦+染料，现改为无序合成，且支持单染和批量两种模式。

**Change**: Vanilla requires fixed pattern for terracotta dyeing. Now shapeless with single and bulk options.

| 模式 | 配方 | 产出 |
|------|------|------|
| 批量 | 8 陶瓦 + 1 染料 | 8 染色陶瓦 |
| 单染 | 1 陶瓦 + 1 染料 | 1 染色陶瓦 |

**配方数量** | **Recipe count**：32（16 色 × 2 种模式）

---

## 🗜️ 方块分解 | Block Decomposition (`data/half/recipe/craft/`)

**新增**：将方块分解回原材料，解决"合成太多无法回收"的问题。

**New**: Decompose blocks back into raw materials.

### 混凝土转换 | Concrete Conversion（16 色 × 2 = 32 配方）

`8 混凝土 + 1 染料 → 8 染色混凝土`
`8 混凝土粉末 + 1 染料 → 8 染色混凝土粉末`

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

## 🔥 烧炼回收 | Smelting Recovery (`data/half/recipe/scrap/`)

**新增**：烧炼粗矿块可直接获得完整金属块，以及混凝土粉末烧成染色玻璃。

**New**: Smelt raw ore blocks directly into metal blocks, and concrete powder into stained glass.

| 原料 | 产物 | 经验 |
|------|------|------|
| 粗铁块 → 铁块 | 6.3 XP |
| 粗铜块 → 铜块 | 6.3 XP |
| 粗金块 → 金块 | 6.3 XP |
| 16 色混凝土粉末 → 对应染色玻璃 | 0.1 XP × 16 |

**配方数量** | **Recipe count**：19

---

## 🏷️ 染料标签 | Dye Tags

数据包定义了 16 种颜色的染料标签（`half:XXX_dyes`），每种标签包含对应颜色的花朵、粉末等所有形态的染料来源，使染色配方兼容各种染料形式。

The datapack defines 16 color dye tags (`half:XXX_dyes`), each containing all dye forms of that color (flowers, powders, etc.), making dyeing recipes compatible with any dye source.

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
| 烧炼回收 Scrap | 19 | 烧炼回收 |
| 简化合成 Simplify | 2 | 简化优化 |
| **总计 Total** | **358** | |

---

> 所有染色配方使用 `half:XXX_dyes` 物品标签，同时兼容原版染料、花朵、墨囊等任意染料来源。  
> All dyeing recipes use `half:XXX_dyes` item tags, compatible with vanilla dyes, flowers, ink sacs, and any dye source.
