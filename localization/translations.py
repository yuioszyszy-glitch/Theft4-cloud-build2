# Theft4 启动器 UI 字符串 英文→中文 映射表
# key 为源码中的原始字符串（含字面 \n 的保持原样），value 为中文译文
TRANSLATIONS = {
    # ===== 大写标题类 =====
    "PLAY": "开始游戏",
    "GRAPHICS": "图形设置",
    "INTERFACE": "界面设置",
    "SYSTEM": "系统设置",
    "MODS": "模组",
    "CONTINUE INTO LIBERTY CITY": "继续进入自由城",
    "ENTER LIBERTY CITY": "进入自由城",
    "INTERNAL RESOLUTION": "内部渲染分辨率",
    "FSR UPSCALING": "FSR 超分辨率",
    "FRAME SPEED": "优先帧率",
    "RESTORE PREVIOUS SETTINGS": "恢复之前的设置",
    "AUTO OPTIMIZE": "自动优化",
    "ORIGINAL · XBOX 360": "原版 · Xbox 360",
    "DYNAMIC SHADOWS": "动态阴影",
    "DRAW DISTANCE": "绘制距离",
    "MODEL DETAIL": "模型细节",
    "REFLECTION QUALITY": "反射质量",
    "ANTI-ALIASING": "抗锯齿",
    "TEXTURE FILTERING · 4×": "纹理过滤 · 4×",
    "MOTION BLUR": "动态模糊",
    "DEPTH OF FIELD": "景深",
    "SHARPENING": "锐化",
    "EXPERIMENTAL FSR BOOST": "实验性 FSR 增强",
    "CPU / THREAD GRAPH": "CPU / 线程图表",
    "FRAME COUNTER": "帧率计数器",
    "FRAME-TIME GRAPH": "帧时间图表",
    "TOUCH CONTROLS": "触控操作",
    "VERIFY GAME FILES": "验证游戏文件",
    "RESTART CORE PROBE": "重启核心检测",
    "DOWNLOAD LATEST LOG CAPTURE": "下载最新日志",
    "EXPORT SAVES TO FILES": "导出存档到“文件”",
    "IMPORT SAVES FROM FILES": "从“文件”导入存档",
    "RUNTIME": "运行环境",
    "SKIP INTRO VIDEOS": "跳过片头视频",
    "LONG PERFORMANCE CAPTURE": "长时间性能记录",
    "SAVE TRANSFER": "存档迁移",
    "ASTC TEXTURE COMPATIBILITY": "ASTC 纹理兼容",
    "DELETE PREPARED TEXTURE CACHE": "删除预处理纹理缓存",
    "CUSTOM TIME CYCLE": "自定义昼夜循环",
    "EXAMPLE SCREENSHOT": "示例截图",
    "MOD DEVELOPER": "模组作者",
    "NATIVE ASPECT RATIO": "原生宽高比",
    "GOD MODE": "无敌模式",
    "UNLIMITED AMMO": "无限弹药",
    "LIGHTING PREVIEW": "光照预览",
    "D-PAD  NAVIGATE     A  SELECT": "十字键 导航     A 确认",
    "IMAGE AND WORLD QUALITY": "画面与世界质量",
    "HUD AND INPUT": "界面与输入",
    "GAME FILES AND RUNTIME": "游戏文件与运行环境",
    "MAKE THE CITY YOUR OWN": "自定义自由城",
    "OPTIMIZED SHADOWS": "优化阴影",
    "ORIGINAL SHADOWS": "原版阴影",
    "ENHANCED SHADOWS": "增强阴影",
    "ULTRA SHADOWS": "极高阴影",
    "OPTIMIZED DISTANCE": "优化距离",
    "ORIGINAL DISTANCE": "原版距离",
    "2× DISTANCE": "2× 距离",
    "3× DISTANCE": "3× 距离",
    "FSR ON": "FSR 开启",
    "FSR OFF": "FSR 关闭",
    "NATIVE ASPECT": "原生比例",
    "NATIVE PIXELS": "原生像素",

    # ===== 句子 / 描述类 =====
    "Optimized": "优化",
    "Original": "原版",
    "Enhanced": "增强",
    "Ultra": "极高",
    "Lower": "较低",
    "Highest": "最高",
    "Full": "完整",
    "Off": "关闭",
    "Native": "原生",
    "Optimized: 0.70× world distance. Reduces how far away world objects are drawn and keeps the game's existing LOD transitions.":
        "优化：0.70× 世界距离。缩短远景物体的绘制距离，并保留游戏原有的 LOD 过渡。",
    "0.70× world distance": "0.70× 世界距离",
    "Optimized: 0.70× world distance and culls far local light volumes. Distant scenery and some night lighting may change.":
        "优化：0.70× 世界距离，并剔除远处局部光源。远景和部分夜间光照可能改变。",
    "0.70× world distance · far local lights reduced": "0.70× 世界距离 · 减少远处局部光源",
    "One more night\nin Liberty City.": "在自由城的\n又一个夜晚。",
    "Cross the river. Take the long way home.\nYour next story starts on these streets.":
        "渡过河流，慢慢回家。\n你的下一段故事，就从这些街道开始。",
    "Continue or begin a new story inside the game. Your saves stay with this app.":
        "在游戏中继续或开启新的故事。你的存档保留在本应用内。",
    "Sharpening strength": "锐化强度",
    "Zero disables sharpening. Changes apply on the next game launch.":
        "设为 0 关闭锐化。更改在下次启动游戏时生效。",
    "Render resolution": "渲染分辨率",
    "The internal scene resolution. Applies at the next game launch.":
        "内部场景分辨率。在下次启动游戏时生效。",
    "By default, choices use centered 16:9. The Native Aspect Ratio mod expands the scene to your screen shape. Native uses physical pixels and disables FSR.":
        "默认选项为居中 16:9。原生宽高比模组可将画面扩展至你的屏幕形状。“原生”使用物理像素并关闭 FSR。",
    "This device uses a fixed 1080p output budget. Lower internal resolutions use FSR 1; changes apply on the next game launch.":
        "本设备使用固定的 1080p 输出。较低的内部分辨率使用 FSR 1；更改在下次启动游戏时生效。",
    "Independent of internal resolution. Off bypasses FSR 1 while keeping the selected scene resolution.":
        "独立于内部分辨率。关闭时绕过 FSR 1，同时保留所选场景分辨率。",
    "Frame Speed keeps your resolution and uses original shadows, earlier resident mesh LOD and shorter draw distance, with edge filters, depth of field and motion blur off. Your selection is kept after reopening.":
        "优先帧率会保留你的分辨率，并使用原版阴影、更早的常驻网格 LOD 和更短的绘制距离，同时关闭边缘滤镜、景深和动态模糊。重新打开后仍保留你的选择。",
    "Auto Optimize for this device": "为此设备自动优化",
    "Original Xbox 360 settings": "原版 Xbox 360 设置",
    "Auto Optimize selects a starting profile for this device. Original restores 720p, original shadow/distance/detail/reflections, and the title's blur. You can adjust each setting afterward.":
        "自动优化会为此设备选择一套初始配置。“原版”恢复 720p、原版阴影/距离/细节/反射和游戏自带的模糊。之后你可以逐项调整。",
    "Dynamic shadows": "动态阴影",
    "Optimized is pending validation of distant shadow cache reuse.":
        "“优化”尚待远处阴影缓存复用的验证。",
    "Draw distance": "绘制距离",
    "Optimized reduces world distance and distant local illumination.":
        "“优化”会降低世界距离和远处局部光照。",
    "Model detail": "模型细节",
    "Lower selects simpler resident meshes sooner without changing draw distance.":
        "“较低”会更早使用简化的常驻网格，但不改变绘制距离。",
    "Reflection resolution": "反射分辨率",
    "Set the renderer's native reflection target preset.":
        "设置渲染器的原生反射目标预设。",
    "Anti-aliasing": "抗锯齿",
    "Select the native renderer's edge smoothing mode.":
        "选择原生渲染器的边缘平滑模式。",
    "Optimized is locked until distant shadow cache reuse is verified. Original: 256 / 2048². Enhanced: 512 / 4096². Ultra: 1024 / up to 8192².":
        "“优化”在远处阴影缓存复用验证前锁定。原版：256 / 2048²；增强：512 / 4096²；极高：1024 / 最高 8192²。",
    "Lower selects simpler resident meshes sooner; Highest prefers the best resident mesh. Neither forces missing models to load. Lower may reduce geometry cost, but CPU gains depend on submesh and draw-call counts.":
        "“较低”更早使用简化常驻网格；“最高”优先最佳常驻网格。两者都不会强制加载缺失模型。“较低”可能降低几何开销，但 CPU 收益取决于子网格和绘制调用数量。",
    "Mirror and water targets / environment cubemap. Full is capped at 1440p in this build.":
        "镜面与水面目标 / 环境立方体贴图。此版本中“完整”上限为 1440p。",
    "Edge smoothing after scene rendering; this does not change internal resolution.":
        "场景渲染后的边缘平滑；不会改变内部分辨率。",
    "Cleaner roads and surfaces at an angle.": "让斜视的路面和物体表面更干净。",
    "Original movement blur. Disable for a sharper image in motion.":
        "原版运动模糊。关闭后运动画面更清晰。",
    "Distance-based focus blur. Off by default on iPhone Air; this may sharpen city views, but performance gains need testing.":
        "基于距离的景深模糊。在 iPhone Air 上默认关闭；可使城市画面更清晰，但性能收益尚待测试。",
    "Graphics changes apply on the next game launch. Extended distance and Ultra shadows can reduce frame rate in dense areas.":
        "图形更改在下次启动游戏时生效。更远的距离和极高阴影在密集场景中可能降低帧率。",
    "1080p ENHANCED OUTPUT": "1080p 增强输出",
    "FSR 1 upscale plus sharpening.": "FSR 1 超分辨率加锐化。",
    "Native-pixel 16:9 output while retaining the 720p scene.": "保留 720p 场景的原生像素 16:9 输出。",
    "Compact device-core and game-thread activity. Updates once per second; included in long captures while enabled.":
        "简洁显示设备核心与游戏线程活动。每秒更新一次；开启后会包含在长时间记录中。",
    "Unique game frames in the top-right corner.": "在右上角显示实际游戏帧数。",
    "Frame delivery against the 33.3 ms target. Double-tap for a short detailed profile. Hold to mark a lag spike or stop and save a long capture.":
        "以 33.3 毫秒为目标的帧输出。双击查看简短详细分析，长按标记卡顿点或停止并保存长时间记录。",
    "Physical controllers continue to work when the overlay is hidden.":
        "隐藏触控层后，实体手柄仍可继续使用。",
    "A connected controller can move focus through this launcher. Use the D-pad or left stick to navigate and A to select.":
        "连接的手柄可在此启动器中移动焦点。用十字键或左摇杆导航，按 A 确认。",
    "Waiting for runtime information…": "正在等待运行信息……",
    "Native ARM64 game code. Your game files. Your city.": "原生 ARM64 游戏代码。你的游戏文件。你的城市。",
    "Skip opening credits and Rockstar logos at the next launch. Game loading still completes normally.":
        "下次启动时跳过开场制作名单和 Rockstar 标志。游戏加载仍会正常完成。",
    "Optimized for normal play. Development logging and probes stay off. Optional graphs and performance captures are available in the launcher.":
        "为正常游玩优化。开发日志和探针保持关闭。可选的图表和性能记录可在启动器中开启。",
    "Off each time the app opens. Enable before Play for up to 5 minutes of timing, without development probes. Turn on the frame-time graph to mark a spike or stop and save; capture also saves when the app goes into the background. Data stays in memory during play.":
        "每次打开应用时默认关闭。在开始游戏前开启，可记录最长 5 分钟的时序（不含开发探针）。打开帧时间图表可标记卡顿或停止并保存；应用进入后台时也会保存记录。游玩期间数据保存在内存中。",
    "Export a dated backup to Files → On My iPhone/iPad → Theft4 → Save Exports. Import a Theft4 save-export folder only while the game is closed; current saves are backed up first.":
        "将带日期的备份导出到 文件 → 我的 iPhone/iPad → Theft4 → Save Exports。仅在游戏关闭时导入 Theft4 存档导出文件夹；当前存档会先被备份。",
    "Automatic one-time setup for this GPU. Saves compressed ASTC copies before Play to reduce texture-conversion pauses and GPU memory use. Later launches reuse them. Devices with direct BC support, such as iPhone 15 Pro (A17 Pro), iPhone 16 (A18), and M3/M4/M5 iPads, skip this requirement.":
        "针对此 GPU 的一次性自动设置。在开始游戏前保存压缩的 ASTC 副本，以减少纹理转换卡顿和显存占用，之后启动会直接复用。支持直接 BC 纹理的设备（如 iPhone 15 Pro (A17 Pro)、iPhone 16 (A18) 及 M3/M4/M5 iPad）可跳过此步骤。",
    "Free the storage used by prepared textures. Confirmation required. Your game files and saves are kept. Devices that need ASTC must prepare textures again before Play.":
        "释放预处理纹理占用的存储空间。需要确认。你的游戏文件和存档会保留。需要 ASTC 的设备在开始游戏前必须重新准备纹理。",
    "Custom Time Cycle example: a bright Liberty City street with a clear blue sky.":
        "自定义昼夜循环示例：晴朗蓝天下明亮的自由城街道。",
    "Developer": "开发者",
    "Developer credit coming soon.": "开发者信息即将推出。",
    "Make Liberty City your own.": "打造属于你的自由城。",
    "Use the bundled time-cycle replacement for lighting, sky, fog and weather appearance. Off uses your original game file.":
        "使用内置的昼夜循环替换来改变光照、天空、雾和天气效果。关闭则使用你的原始游戏文件。",
    "Actual appearance varies with the time of day, weather and your graphics settings. This mod changes atmosphere settings; it does not replace textures.":
        "实际效果随一天中的时间、天气和你的图形设置而变化。此模组改变的是氛围参数，不替换纹理。",
    "Expand the game view to your screen: more scenery above and below on iPad, or at the sides on wider iPhones. Preserves proportions without cropping or stretching.":
        "将游戏画面扩展至你的屏幕：iPad 上显示更多上下景物，更宽的 iPhone 上显示更多两侧景物。保持比例，不裁剪、不拉伸。",
    "Camera projection and visibility expand with the viewport. HUD and phone keep their proportions and respect screen safe areas. Extra scenery and pixels can increase rendering cost. Off restores original 16:9 framing.":
        "相机投影和可见范围随视口扩展。HUD 和手机界面保持比例并遵循屏幕安全区域。额外的景物和像素会增加渲染开销。关闭则恢复原始 16:9 画面。",
    "The view follows the window shape when you press Play. If you rotate or resize afterward, it keeps that shape; reopen to fill the new window. Videos and fixed artwork keep their original proportions.":
        "画面在你按下开始游戏时跟随窗口形状。之后旋转或调整大小会保持该形状；重新打开以填满新窗口。视频和固定画面保持原始比例。",
    "Protect your player from damage and death, including bullets, explosions, fire, collisions and drowning. Other characters remain vulnerable.":
        "保护你的角色免受伤害和死亡，包括子弹、爆炸、火焰、碰撞和溺水。其他角色仍会受到伤害。",
    "Keep reserve ammunition for weapons you own. Magazines still empty, and you still reload normally. This does not grant weapons.":
        "保留你已有武器的备用弹药。弹匣仍会打空，仍需正常换弹。此功能不会提供武器。",
    "Reserve ammo is replenished while enabled. Replenished ammo amounts can be included in your game save; turning the mod off restores normal ammo consumption.":
        "开启时备用弹药会自动补充。补充的弹药数量可计入游戏存档；关闭此模组则恢复正常弹药消耗。",
    "Applies when you press Play in a fresh app session. To change it after playing, save, close Theft4 and reopen. Your original game files and saves are kept.":
        "在全新的应用会话中按下开始游戏时生效。游玩后想更改，请先保存、关闭 Theft4 再重新打开。你的原始游戏文件和存档会保留。",
    "Appearance varies with weather and time of day.": "外观随天气和一天中的时间而变化。",
    "Bundled lighting, sky, fog and weather replacement. Off uses the original game file.":
        "内置光照、天空、雾和天气替换。关闭则使用原始游戏文件。",
    "Fill your screen with extra scenery, without stretching or cropping.":
        "用更多景物填满你的屏幕，不拉伸、不裁剪。",
    "HUD keeps its proportions. Extra scenery can cost performance. Videos keep their original shape; reopen after rotating or resizing.":
        "HUD 保持比例。额外景物会消耗性能。视频保持原始形状；旋转或调整大小后请重新打开。",
    "No player damage or death. Other characters remain vulnerable.": "角色不受伤害、不会死亡。其他角色仍会受到伤害。",
    "Unlimited reserve ammo. Magazines still empty and reload normally. No weapons granted.":
        "无限备用弹药。弹匣仍会打空并正常换弹。不提供武器。",
    "Replenished ammo can be saved. Turning the mod off restores normal consumption.":
        "补充的弹药可保存。关闭此模组则恢复正常消耗。",
    "Choose before Play. Save and reopen the app to change mods after playing.":
        "请在开始游戏前选择。游玩后想更改模组，请保存并重新打开应用。",
    "Core ready": "核心就绪",
    "LIBERTY CITY, AFTER DARK\nDRAG TO ORBIT · PINCH TO ZOOM": "自由城，夜幕降临\n拖动旋转 · 双指缩放",
    "Liberty City awaits.": "自由城在等你。",
    "128 base · 1024 × 1024 cache · 0.75× range": "128 基础 · 1024 × 1024 缓存 · 0.75× 范围",
    "256 base · 2048 × 2048 cache · 1× range": "256 基础 · 2048 × 2048 缓存 · 1× 范围",
    "512 base · 4096 × 4096 cache · 1× range": "512 基础 · 4096 × 4096 缓存 · 1× 范围",
    "1024 base · up to 8192 × 8192 cache · 1.5× range": "1024 基础 · 最高 8192 × 8192 缓存 · 1.5× 范围",
    "1× world distance · 13,000 drawable references": "1× 世界距离 · 13,000 可绘制引用",
    "2× world distance · 17,000 drawable references": "2× 世界距离 · 17,000 可绘制引用",
    "3× world distance · 20,000 drawable references": "3× 世界距离 · 20,000 可绘制引用",
    "320 × 180 mirror/water · 256² environment": "320 × 180 镜面/水面 · 256² 环境",
    "1920 × 1080 mirror/water · 1024² environment": "1920 × 1080 镜面/水面 · 1024² 环境",
    "2560 × 1440 mirror/water · 2048² environment": "2560 × 1440 镜面/水面 · 2048² 环境",
    "Earlier transition to simpler resident meshes · 1.75× selector input": "更早过渡到简化常驻网格 · 1.75× 选择器输入",
    "Highest resident mesh at any distance": "任何距离都使用最高常驻网格",
    "Title-controlled model LOD": "由游戏控制的模型 LOD",
    "No edge filter": "无边缘滤镜",
    "FXAA · single lightweight pass": "FXAA · 单次轻量处理",
    "SMAA 1× · high preset": "SMAA 1× · 高预设",
}
