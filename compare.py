import json, os, sys
sys.stdout.reconfigure(encoding='utf-8')

backup = r'd:\backup\saves\xsh\datapacks\RCraft-0.8.1-data-mc1.21.1'
github = r'd:\cloade\github\src'

def get_recipes(base):
    """返回 {(namespace, path): full_path} 的字典"""
    result = {}
    for root, dirs, files in os.walk(base):
        for f in files:
            if not f.endswith('.json'):
                continue
            fp = os.path.join(root, f)
            rel = os.path.relpath(fp, base)
            parts = rel.split(os.sep)
            # 找到 data/namespace/recipe/... 的结构
            if 'recipe' in parts:
                ri = parts.index('recipe')
                ns = parts[ri - 1]  # namespace
                recipe_path = '/'.join(parts[ri+1:])
                result[(ns, recipe_path)] = fp
            # github 中可能有外层模块目录
            if len(parts) > 2 and parts[2] == 'data':
                ns2 = parts[3] if len(parts) > 3 else 'unknown'
                if 'recipe' in parts[4:]:
                    ri2 = parts[4:].index('recipe') + 4
                    recipe_path2 = '/'.join(parts[ri2+1:])
                    result[(ns2, recipe_path2)] = fp
    return result

# 备份版本的配方
backup_recipes = {}
for root, dirs, files in os.walk(backup):
    for f in files:
        if not f.endswith('.json'):
            continue
        fp = os.path.join(root, f)
        rel = os.path.relpath(fp, backup)
        parts = rel.replace('\\', '/').split('/')
        if 'recipe' in parts:
            ri = parts.index('recipe')
            if ri >= 2:
                ns = parts[ri - 1]
                recipe_path = '/'.join(parts[ri+1:])
                backup_recipes[(ns, recipe_path)] = fp

# github 的配方
github_recipes = {}
for root, dirs, files in os.walk(github):
    for f in files:
        if not f.endswith('.json'):
            continue
        fp = os.path.join(root, f)
        rel = os.path.relpath(fp, github)
        parts = rel.replace('\\', '/').split('/')
        # github 结构: module/data/namespace/recipe/...
        if 'recipe' in parts:
            ri = parts.index('recipe')
            if ri >= 2:
                ns = parts[ri - 1]
                recipe_path = '/'.join(parts[ri+1:])
                github_recipes[(ns, recipe_path)] = fp

print(f"备份配方数: {len(backup_recipes)}")
print(f"Github配方数: {len(github_recipes)}")

# 找出备份中有但github中没有的
only_backup = set(backup_recipes.keys()) - set(github_recipes.keys())
if only_backup:
    print(f"\n=== 备份中有但Github中缺失的配方 ({len(only_backup)}个) ===")
    for key in sorted(only_backup):
        print(f"  [{key[0]}] {key[1]}")

# 找出github中有但备份中没有的
only_github = set(github_recipes.keys()) - set(backup_recipes.keys())
if only_github:
    print(f"\n=== Github中有但备份中没有的配方 ({len(only_github)}个) ===")
    for key in sorted(only_github):
        print(f"  [{key[0]}] {key[1]}")

# 比较共同配方的内容差异
common = set(backup_recipes.keys()) & set(github_recipes.keys())
changed = []
for key in sorted(common):
    bp = backup_recipes[key]
    gp = github_recipes[key]
    try:
        with open(bp, 'r', encoding='utf-8') as f:
            bd = json.load(f)
        with open(gp, 'r', encoding='utf-8') as f:
            gd = json.load(f)
        # 去掉 _note 字段比较
        bd.pop('_note', None)
        gd.pop('_note', None)
        if bd != gd:
            changed.append(key)
    except:
        changed.append(key)

if changed:
    print(f"\n=== 内容不同的配方 ({len(changed)}个) ===")
    for key in changed:
        print(f"  [{key[0]}] {key[1]}")
else:
    print(f"\n所有共同配方({len(common)}个)内容一致（忽略_note字段）")
