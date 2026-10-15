"""Simplified Chinese translations for user-facing download status messages.

Core errors are preserved in their original language in the diagnostic log;
this translator only changes text rendered in the GUI.
"""
EXACT = dict([
    [
        "Session loaded successfully!",
        "会话文件加载成功！"
    ],
    [
        "Login successful!",
        "登录成功！"
    ],
    [
        "Two-factor authentication successful!",
        "双重身份验证成功！"
    ],
    [
        "Two-factor authentication required. Please enter the code.",
        "需要双重身份验证，请输入验证码。"
    ],
    [
        "Login successful without 2FA",
        "登录成功，无需双重身份验证。"
    ],
    [
        "Starting to download posts matching criteria...",
        "开始下载符合条件的帖子…"
    ],
    [
        "Rate limited by Instagram! Taking a longer break...",
        "Instagram 已限制请求频率，正在延长等待时间…"
    ],
    [
        "Story download blocked - likely rate limited",
        "快拍下载被阻止，可能触发了请求限制。"
    ],
    [
        "Story not found. It may be expired or private.",
        "未找到快拍，可能已过期或账号为私密状态。"
    ],
    [
        "Fetching saved posts...",
        "正在获取已收藏的帖子…"
    ],
    [
        "Starting Saved Posts download...",
        "开始下载已收藏帖子…"
    ],
    [
        "Single item download completed successfully!",
        "单条内容下载成功！"
    ],
    [
        "Single item download failed.",
        "单条内容下载失败。"
    ],
    [
        "Download process completed!",
        "全部下载任务已完成！"
    ],
    [
        "Download stopped by user",
        "下载已由用户停止。"
    ],
    [
        "Download paused by user",
        "用户已暂停下载。"
    ],
    [
        "Download resumed by user",
        "用户已继续下载。"
    ],
    [
        "Download process resumed from pause",
        "下载任务已继续。"
    ],
    [
        "Download process paused - Use Resume button to continue",
        "下载任务已暂停，点击“继续”恢复。"
    ],
    [
        "Profile doesn't exist",
        "账号不存在。"
    ],
    [
        "Profile not found",
        "未找到账号。"
    ],
    [
        "Login required to view",
        "需要登录才能查看。"
    ],
    [
        "Network error or rate limited",
        "网络错误或触发了请求限制。"
    ],
    [
        "Login required to check",
        "请先登录才能检查账号。"
    ],
    [
        "Session file not found!",
        "找不到会话文件！"
    ],
    [
        "No saved settings found",
        "没有已保存的设置。"
    ],
    [
        "Settings loaded successfully",
        "设置加载成功。"
    ],
    [
        "Settings restored from backup",
        "已从备份恢复设置。"
    ],
    [
        "Error: Could not extract post ID from URL",
        "错误：无法从链接中识别帖子 ID。"
    ],
    [
        "Unrecognized URL format",
        "无法识别的链接格式。"
    ],
    [
        "Skipping existing profile picture",
        "正在跳过已有头像。"
    ],
    [
        "Successfully downloaded profile picture",
        "头像下载成功！"
    ],
    [
        "Unable to determine total post count, using default value",
        "无法取得帖子总数，使用默认预估值。"
    ],
    [
        "No 2FA code provided or timeout",
        "未输入验证码或等待超时。"
    ],
    [
        "Two-factor authentication failed: No code provided or timeout",
        "双重身份验证失败：未输入验证码或等待超时。"
    ],
    [
        "Advanced settings reset to default values",
        "高级设置已恢复默认值。"
    ],
    [
        "Download thread stop requested",
        "已请求停止下载任务。"
    ],
    [
        "Download canceled during 2FA",
        "双重验证期间已取消下载。"
    ],
    [
        "Login required to check profile",
        "检查账号需要先登录。"
    ]
])
PREFIXES = [
    [
        "Session saved to ",
        "会话文件已保存至："
    ],
    [
        "Warning: Could not save session file: ",
        "警告：无法保存会话文件："
    ],
    [
        "Session file not found: ",
        "未找到会话文件："
    ],
    [
        "Authentication failed: ",
        "身份验证失败："
    ],
    [
        "Bad credentials: ",
        "账号或密码错误："
    ],
    [
        "Login error: ",
        "登录错误："
    ],
    [
        "Two-factor authentication failed: ",
        "双重身份验证失败："
    ],
    [
        "Initializing single post download: ",
        "正在初始化单条内容下载："
    ],
    [
        "Initializing profile download: ",
        "正在初始化账号下载："
    ],
    [
        "Loading session file for user: ",
        "正在载入账号会话："
    ],
    [
        "Logging in with credentials for user: ",
        "正在使用账号密码登录："
    ],
    [
        "Saving session file to ",
        "正在保存会话文件至："
    ],
    [
        "Failed to save session: ",
        "保存会话失败："
    ],
    [
        "Error during 2FA login: ",
        "双重验证登录失败："
    ],
    [
        "Could not extract username from session file: ",
        "无法从会话文件提取用户名："
    ],
    [
        "Found ",
        "发现 "
    ],
    [
        "Estimated total posts: ",
        "预计帖子数量："
    ],
    [
        "Adjusting estimated total to ",
        "正在调整预估总数为："
    ],
    [
        "Reached the maximum number of posts limit ",
        "已达到最大帖子数量限制 "
    ],
    [
        "Reached limit of ",
        "已达到下载上限 "
    ],
    [
        "Skipping existing post from ",
        "跳过已存在的帖子，日期："
    ],
    [
        "Processing post ",
        "正在处理帖子 "
    ],
    [
        "Successfully downloaded post from ",
        "帖子下载成功，日期："
    ],
    [
        "Downloading post from ",
        "正在下载帖子，日期："
    ],
    [
        "Error downloading post: ",
        "帖子下载失败："
    ],
    [
        "Failed to download post after ",
        "帖子多次下载失败，已尝试 "
    ],
    [
        "Long session safety delay: ",
        "长休息安全等待："
    ],
    [
        "Safety pause: ",
        "安全等待："
    ],
    [
        "Connection error: ",
        "连接错误："
    ],
    [
        "Processing posts in date range: ",
        "正在处理日期范围内的帖子："
    ],
    [
        "Reached posts older than the specified date range, stopping",
        "已到达筛选日期以前的帖子，停止。"
    ],
    [
        "Skipping existing highlight item from ",
        "跳过已存在的精选动态，日期："
    ],
    [
        "Successfully downloaded highlight item from ",
        "精选动态下载成功，日期："
    ],
    [
        "Error downloading highlight item: ",
        "精选动态下载失败："
    ],
    [
        "Downloaded ",
        "已下载 "
    ],
    [
        "Error downloading highlights: ",
        "精选动态下载失败："
    ],
    [
        "Skipping existing story item from ",
        "跳过已存在的快拍，日期："
    ],
    [
        "Successfully downloaded story item from ",
        "快拍下载成功，日期："
    ],
    [
        "Error downloading story item: ",
        "快拍下载失败："
    ],
    [
        "Error accessing stories: ",
        "访问快拍时出错："
    ],
    [
        "Fetching post with ID: ",
        "正在获取帖子 ID："
    ],
    [
        "Post belongs to user: ",
        "帖子所属用户："
    ],
    [
        "Error fetching post: ",
        "获取帖子失败："
    ],
    [
        "Fetching reel with ID: ",
        "正在获取 Reels ID："
    ],
    [
        "Reel belongs to user: ",
        "Reels 所属用户："
    ],
    [
        "Skipping existing reel from ",
        "跳过已存在的 Reels，日期："
    ],
    [
        "Downloading reel from ",
        "正在下载 Reels，日期："
    ],
    [
        "Successfully downloaded reel from ",
        "Reels 下载成功，日期："
    ],
    [
        "Error fetching reel: ",
        "获取 Reels 失败："
    ],
    [
        "Fetching story from user ",
        "正在获取用户快拍："
    ],
    [
        "Found story with ID ",
        "已找到快拍 ID "
    ],
    [
        "Successfully downloaded story from ",
        "快拍下载成功，日期："
    ],
    [
        "Error fetching story: ",
        "获取快拍失败："
    ],
    [
        "Got profile name from URL: ",
        "从链接识别账号："
    ],
    [
        "Using provided highlight owner: ",
        "使用指定的精选动态所属用户："
    ],
    [
        "Using logged in username: ",
        "使用已登录用户名："
    ],
    [
        "Downloading ",
        "正在下载 "
    ],
    [
        "Error downloading item ",
        "下载项目出错 "
    ],
    [
        "Skipping existing saved post from ",
        "跳过已收藏的已有帖子："
    ],
    [
        "Processing saved post ",
        "正在处理已收藏帖子 "
    ],
    [
        "Successfully downloaded saved post from ",
        "已收藏帖子下载成功，日期："
    ],
    [
        "Error downloading saved post: ",
        "已收藏帖子下载失败："
    ],
    [
        "Downloading to ",
        "下载目录："
    ],
    [
        "Extracted highlight owner from URL: ",
        "从链接中识别精选动态用户："
    ],
    [
        "Processing single item URL: ",
        "正在处理单条内容链接："
    ],
    [
        "Error: ",
        "错误："
    ],
    [
        "Login required to view ",
        "需要登录才能查看 "
    ],
    [
        "Error checking profile ",
        "检查账号时出错 "
    ],
    [
        "Profile check failed: ",
        "账号检查失败："
    ],
    [
        "No saved settings found",
        "没有找到已保存的设置"
    ],
    [
        "Error loading backup settings: ",
        "载入备份设置失败："
    ],
    [
        "Error loading settings and backup: ",
        "设置与备份均无法载入："
    ],
    [
        "Error loading settings: ",
        "加载设置失败："
    ],
    [
        "Error saving settings: ",
        "保存设置失败："
    ],
    [
        "Settings saved to ",
        "设置已保存至："
    ],
    [
        "Invalid Instagram URL format.",
        "Instagram 链接格式无效。"
    ],
    [
        "Session file has been set for next download.",
        "已设置下一次下载使用的会话文件。"
    ],
    [
        "Target profile name is required!",
        "必须输入目标用户名！"
    ],
    [
        "Please enter a username",
        "请输入用户名"
    ]
]

def translate_log(message):
    """Return a Chinese UI message while preserving paths, usernames and exception details."""
    if not isinstance(message, str):
        return str(message)
    if message in EXACT:
        return EXACT[message]
    for english, chinese in sorted(PREFIXES, key=lambda item: len(item[0]), reverse=True):
        if message.startswith(english):
            return chinese + message[len(english):]
    return message
