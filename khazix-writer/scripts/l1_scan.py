"""
L1 硬性规则全量扫描脚本
必须运行全部 5 项检查，L1-5 是最高频漏检项。
"""

import re
import sys

def scan(path):
    with open(path, "r") as f:
        content = f.read()

    all_clean = True

    # === L1-1: 禁用词 ===
    banned_words = [
        "说白了", "本质上", "换句话说", "不可否认",
        "值得注意的是", "不难发现", "综上所述", "总的来说",
        "让我们来看看", "接下来让我们",
    ]
    print("=== L1-1 禁用词 ===")
    hits = []
    for w in banned_words:
        count = content.count(w)
        if count > 0:
            hits.append(f"  ❌ '{w}' x{count}")
    if hits:
        for h in hits:
            print(h)
        all_clean = False
    else:
        print("  ✅ 零命中")

    # === L1-2: 禁用标点 ===
    punct_map = {
        "：": "冒号", "——": "破折号",
        "\u201c": "左双引号", "\u201d": "右双引号",
        '"': "英文双引号",
    }
    print("\n=== L1-2 禁用标点 ===")
    punct_hits = []
    for ch, name in punct_map.items():
        count = content.count(ch)
        if count > 0:
            punct_hits.append(f"  ❌ {name}「{ch}」x{count}")
    if punct_hits:
        for h in punct_hits:
            print(h)
        all_clean = False
    else:
        print("  ✅ 零命中")

    # === L1-3: 结构性套话 ===
    struct_patterns = [
        "让我们来看看", "在当今", "随着.*的发展",
    ]
    print("\n=== L1-3 结构性套话 ===")
    struct_hits = []
    for pat in struct_patterns:
        matches = re.findall(pat, content)
        if matches:
            struct_hits.append(f"  ❌ '{pat}' x{len(matches)}")
    if struct_hits:
        for h in struct_hits:
            print(h)
        all_clean = False
    else:
        print("  ✅ 零命中")

    # === L1-4: 空泛工具名 ===
    vague_tools = ["AI工具", "某个模型", "相关技术"]
    print("\n=== L1-4 空泛工具名 ===")
    vague_hits = []
    for t in vague_tools:
        if t in content:
            vague_hits.append(f"  ❌ '{t}'")
    if vague_hits:
        for h in vague_hits:
            print(h)
        all_clean = False
    else:
        print("  ✅ 零命中")

    # === L1-5: 矫正句式 ⚠️ 最高频漏检 ===
    print("\n=== L1-5 矫正句式「不是/既不是」⚠️ ===")
    issues = []
    lines_list = content.split('\n')
    for i, line in enumerate(lines_list, 1):
        stripped = line.strip()
        if not stripped:
            continue
        if re.search(r'(?:不是|既不是)', stripped):
            # 豁免「」内的受访者原话
            quotes = re.findall(r'「[^」]*(?:不是|既不是)[^」]*」', stripped)
            if quotes:
                continue
            # 豁免疑问句
            if re.search(r'是不是[^？?]*[？?]$', stripped):
                continue
            # 豁免短句单纯否定（如"它不是人。"，不构成"不是X，是Y"矫正结构）
            if len(stripped) < 20 and not re.search(r'(?:不是|既不是).*(?:而是|，是|。是)', stripped):
                # 短句 + 无后续"而是/是" → 可能只是单纯否定，检查上下文
                next_line = lines_list[i] if i < len(lines_list) else ""
                prev_line = lines_list[i-2] if i >= 2 else ""
                if not re.search(r'(?:而是|，是|。是)', next_line) and not re.search(r'(?:不是|既不是).*(?:而是)', prev_line + stripped + next_line):
                    continue
            issues.append(f"  L{i}: {stripped[:80]}")
    if issues:
        for iss in issues:
            print(iss)
        print(f"\n  ⚠️ 共 {len(issues)} 处需改写")
        all_clean = False
    else:
        print("  ✅ 零命中（引用内豁免除外）")

    print(f"\n=== L1 总评: {'✅ 全部通过' if all_clean else '❌ 需要修复'} ===")
    return all_clean

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python l1_scan.py <article.md>")
        sys.exit(1)
    scan(sys.argv[1])
