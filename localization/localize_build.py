"""在云构建中，把启动器源码里的英文 UI 字符串替换为中文。
在 working-directory = Theft4（源码根目录）下运行：
    python "$GITHUB_WORKSPACE/localization/localize_build.py"
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from translations import TRANSLATIONS
from translations_main import TRANSLATIONS_MAIN


def to_source(s):
    # 真换行 → 字面 \n（Objective-C 源码写法）
    return s.replace('\n', '\\n')


def localize(path, mapping):
    if not os.path.exists(path):
        print(f'[跳过] 文件不存在: {path}', flush=True)
        return 0
    text = open(path, encoding='utf-8').read()
    count = 0
    missing = []
    for en, zh in mapping.items():
        old = '@"' + to_source(en) + '"'
        new = '@"' + to_source(zh) + '"'
        if old in text:
            text = text.replace(old, new)
            count += 1
        else:
            missing.append(en)
    open(path, 'w', encoding='utf-8').write(text)
    print(f'{path}: 汉化 {count} 处, 未命中 {len(missing)}', flush=True)
    for m in missing:
        print('   未命中:', repr(m[:70]), flush=True)
    return count


def main():
    total = 0
    total += localize('ios/Theft4/Theft4LauncherView.m', TRANSLATIONS)
    total += localize('ios/Theft4/main.m', TRANSLATIONS_MAIN)
    print(f'汉化完成，共替换 {total} 处', flush=True)


if __name__ == '__main__':
    main()
