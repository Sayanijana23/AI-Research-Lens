css = """
<style>
:root {
    color-scheme: dark;
    --rp-bg: #040b18;
    --rp-bg-2: #071a2b;
    --rp-panel: rgba(12, 18, 31, 0.78);
    --rp-panel-strong: rgba(16, 23, 38, 0.96);
    --rp-text: #eef3ff;
    --rp-muted: #b7c7e5;
    --rp-border: rgba(125, 107, 255, 0.38);
    --rp-accent: #b38bff;
    --rp-accent-2: #5ae0ff;
    --rp-accent-3: #f1a2ff;
    --rp-user-bg: rgba(143, 115, 255, 0.18);
    --rp-assistant-bg: rgba(17, 24, 39, 0.9);
    --rp-source-bg: rgba(13, 18, 29, 0.8);
    --rp-shadow: rgba(111, 107, 255, 0.16);
}

html, body {
    background: linear-gradient(180deg, #030b18 0%, #050d1d 100%) !important;
}

.stApp,
[data-testid="stAppViewContainer"],
[data-testid="stHeader"],
[data-testid="stToolbar"] {
    background: radial-gradient(circle at 24% 18%, rgba(130, 94, 255, 0.22), transparent 26%),
                radial-gradient(circle at 80% 14%, rgba(79, 196, 255, 0.18), transparent 20%),
                linear-gradient(180deg, #030b18 0%, #071224 48%, #040b19 100%) !important;
    color: var(--rp-text) !important;
}

.stApp::before {
    content: "";
    position: fixed;
    inset: 0;
    background-image:
        radial-gradient(circle, rgba(255,255,255,0.7) 1px, transparent 2px),
        radial-gradient(circle, rgba(139,95,255,0.8) 1px, transparent 2px),
        radial-gradient(circle, rgba(56,206,255,0.9) 1px, transparent 2px);
    background-size: 220px 220px;
    background-position: 0 0, 80px 90px, 110px 30px;
    opacity: 0.38;
    pointer-events: none;
}

.main .block-container {
    max-width: 1500px;
    padding-top: 0.5rem;
    padding-bottom: 2rem;
}

h1, h2, h3, h4, h5, h6,
p, li, label,
[data-testid="stMarkdownContainer"],
[data-testid="stWidgetLabel"] {
    color: var(--rp-text) !important;
}

a {
    color: var(--rp-accent) !important;
}

code,
pre {
    background-color: var(--rp-panel-strong) !important;
    color: var(--rp-text) !important;
    border-radius: 6px;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, rgba(9, 16, 30, 0.96), rgba(14, 21, 39, 0.94)) !important;
    border-right: 1px solid rgba(141, 92, 246, 0.35) !important;
    box-shadow: inset -1px 0 0 rgba(148, 163, 184, 0.12);
}

[data-testid="stSidebar"] * {
    color: #edf2ff;
}

[data-testid="stSidebar"] [data-testid="stBaseButton-secondary"],
[data-testid="stSidebar"] button,
[data-testid="stSidebar"] .stButton > button,
.stTextInput input,
.stNumberInput input,
.stTextArea textarea,
[data-baseweb="input"] input,
[data-baseweb="textarea"] textarea,
.stSelectbox div[data-baseweb="select"] > div,
.stSelectbox [data-baseweb="select"] > div,
.stSelectbox > div > div,
[data-testid="stChatInput"],
[data-testid="stChatInput"] textarea {
    background-color: rgba(14, 20, 38, 0.8) !important;
    border-color: rgba(141, 92, 246, 0.45) !important;
    color: #111827 !important;
}

.stSelectbox [data-baseweb="select"] > div > div,
.stSelectbox [data-baseweb="select"] > div > span,
.stSelectbox [data-baseweb="select"] [role="button"],
.stSelectbox [data-baseweb="select"] * {
    color: #111827 !important;
}

.stTextInput input::placeholder,
.stTextArea textarea::placeholder,
[data-testid="stChatInput"] textarea::placeholder {
    color: var(--rp-muted) !important;
}

[data-baseweb="popover"],
[data-baseweb="popover"] > div,
[data-baseweb="popover"] [data-baseweb="block"],
[data-baseweb="popover"] [data-baseweb="menu"],
[data-baseweb="menu"],
[data-testid="stMainMenu"],
[data-testid="stMainMenu"] *,
[role="listbox"],
[role="option"],
[role="menu"],
[role="menuitem"] {
    background-color: rgba(15, 23, 42, 0.95) !important;
    color: var(--rp-text) !important;
}

[role="option"]:hover,
[role="option"][aria-selected="true"],
[role="menuitem"]:hover {
    background-color: rgba(141, 92, 246, 0.20) !important;
    color: var(--rp-text) !important;
}

[data-testid="stMainMenu"] button,
[data-testid="stMainMenu"] div,
[data-testid="stMainMenu"] span,
[data-testid="stMainMenu"] p,
[data-baseweb="popover"] button,
[data-baseweb="popover"] div,
[data-baseweb="popover"] span,
[data-baseweb="popover"] p {
    color: var(--rp-text) !important;
}

.stButton button {
    background: linear-gradient(135deg, rgba(141, 92, 246, 0.95), rgba(111, 90, 255, 0.9)) !important;
    border: 1px solid rgba(168, 85, 247, 0.8) !important;
    color: white !important;
    border-radius: 12px;
    box-shadow: 0 0 18px rgba(141, 92, 246, 0.25);
}

.stButton button:hover {
    background: linear-gradient(135deg, rgba(168, 85, 247, 1), rgba(139, 92, 246, 1)) !important;
    border-color: rgba(34, 211, 238, 0.6) !important;
    color: white !important;
}

[data-testid="stFileUploader"] section,
[data-testid="stFileUploaderDropzone"] {
    background: rgba(10, 16, 29, 0.6) !important;
    border: 1px dashed rgba(141, 92, 246, 0.6) !important;
    color: var(--rp-text) !important;
}

.selected-file-list {
    margin-top: 0.6rem;
    display: flex;
    flex-direction: column;
    gap: 0.45rem;
}

.selected-file-item {
    background: rgba(255, 255, 255, 0.08);
    color: #eaf0ff;
    border: 1px solid rgba(141, 92, 246, 0.35);
    border-radius: 10px;
    padding: 0.5rem 0.7rem;
    font-size: 0.92rem;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}

[data-testid="stFileUploader"] small,
[data-testid="stFileUploader"] span,
[data-testid="stFileUploaderDropzoneInstructions"] {
    color: var(--rp-muted) !important;
}

.chat-container {
    max-width: 900px;
    margin: auto;
}

.top-bar {
    display: flex;
    justify-content: flex-end;
    align-items: center;
    gap: 14px;
    margin-top: 0.2rem;
    margin-bottom: 1.5rem;
}

.deploy-btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
    min-width: 130px;
    padding: 0.7rem 1.1rem;
    border-radius: 14px;
    border: 1px solid rgba(141, 92, 246, 0.8);
    background: rgba(9, 14, 26, 0.4);
    color: var(--rp-text);
    font-weight: 600;
    box-shadow: inset 0 0 0 1px rgba(255,255,255,0.03), 0 0 18px rgba(141, 92, 246, 0.12);
}

.toolbar-icon {
    width: 38px;
    height: 38px;
    border-radius: 50%;
    border: 1px solid rgba(141, 92, 246, 0.7);
    display: flex;
    align-items: center;
    justify-content: center;
    background: rgba(17, 24, 39, 0.7);
    color: var(--rp-text);
    font-size: 1rem;
    box-shadow: 0 0 12px rgba(141, 92, 246, 0.18);
}

.hero-shell {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 2rem 1rem 1.2rem;
    position: relative;
}

.hero-title {
    font-size: clamp(2.8rem, 4vw, 5rem);
    font-weight: 800;
    line-height: 1.05;
    letter-spacing: -0.045em;
    margin: 0;
    color: #eaf0ff;
    text-shadow: none;
}

.hero-title .spark {
    display: none;
}

.hero-divider {
    width: 210px;
    height: 3px;
    border-radius: 999px;
    margin: 1.2rem auto 1.1rem;
    background: linear-gradient(90deg, rgba(154, 123, 255, 0.9), rgba(55, 203, 255, 0.9), rgba(154, 123, 255, 0.3));
    box-shadow: 0 0 16px rgba(111, 182, 255, 0.35);
}

.hero-copy {
    max-width: 720px;
    color: rgba(230, 236, 255, 0.82);
    font-size: clamp(1rem, 1.5vw, 1.3rem);
    line-height: 1.6;
    margin: 0 auto 1.5rem;
}

.hero-visual {
    position: relative;
    width: min(65vw, 720px);
    height: 290px;
    margin: 0 auto 1.7rem;
    display: flex;
    align-items: center;
    justify-content: center;
}

.hero-book {
    position: relative;
    width: 360px;
    height: 180px;
    border-radius: 22px;
    background: linear-gradient(135deg, rgba(34, 211, 238, 0.22), rgba(141, 92, 246, 0.14));
    border: 2px solid rgba(52, 212, 255, 0.7);
    box-shadow: 0 0 24px rgba(52, 212, 255, 0.2), 0 0 48px rgba(141, 92, 246, 0.18);
    transform: perspective(1100px) rotateX(12deg) rotateY(-12deg);
}

.hero-book::before,
.hero-book::after {
    content: "";
    position: absolute;
    inset: 0;
    border-radius: 22px;
}

.hero-book::before {
    background: linear-gradient(135deg, rgba(52, 212, 255, 0.18), rgba(141, 92, 246, 0.15));
    border: 2px solid rgba(141, 92, 246, 0.5);
    transform: scale(1.02) translateY(8px);
}

.hero-book::after {
    inset: 18px 18px 18px 26px;
    background: linear-gradient(135deg, rgba(17, 24, 39, 0.9), rgba(11, 18, 31, 0.8));
    border: 1px solid rgba(52, 212, 255, 0.4);
    border-radius: 16px;
    box-shadow: inset 0 0 18px rgba(52, 212, 255, 0.12);
}

.hero-pdf {
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-120%, -6%);
    width: 116px;
    height: 120px;
    border-radius: 12px;
    background: linear-gradient(135deg, rgba(18, 25, 41, 0.9), rgba(147, 51, 234, 0.32));
    border: 1px solid rgba(141, 92, 246, 0.7);
    box-shadow: 0 0 20px rgba(141, 92, 246, 0.25);
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 800;
    color: var(--rp-text);
    font-size: 2rem;
}

.hero-pdf::before {
    content: "PDF";
}

.hero-chat-bubble {
    position: absolute;
    left: 50%;
    top: 34%;
    transform: translate(-202%, -30%);
    width: 88px;
    height: 54px;
    border-radius: 12px;
    background: rgba(8, 14, 24, 0.75);
    border: 1px solid rgba(52, 212, 255, 0.5);
    box-shadow: 0 0 18px rgba(52, 212, 255, 0.12);
}

.hero-chat-bubble::before,
.hero-chat-bubble::after {
    content: "";
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    bottom: -8px;
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background: rgba(52, 212, 255, 0.9);
    box-shadow: 0 0 8px rgba(52, 212, 255, 0.8);
}

.hero-chat-bubble::before {
    left: 24%;
    width: 8px;
    height: 8px;
    opacity: 0.8;
}

.hero-chat-bubble::after {
    left: 50%;
    width: 14px;
    height: 14px;
    opacity: 0.9;
}

.hero-search {
    position: absolute;
    right: 18%;
    top: 34%;
    width: 110px;
    height: 110px;
    border-radius: 50%;
    border: 2px solid rgba(141, 92, 246, 0.7);
    box-shadow: 0 0 26px rgba(141, 92, 246, 0.18);
}

.hero-search::before,
.hero-search::after {
    content: "";
    position: absolute;
}

.hero-search::before {
    width: 58px;
    height: 2px;
    background: rgba(52,212,255,0.9);
    transform: rotate(45deg);
    right: 18px;
    top: 62px;
    border-radius: 999px;
}

.hero-search::after {
    width: 28px;
    height: 28px;
    border: 3px solid rgba(52, 212, 255, 0.95);
    border-radius: 50%;
    left: 25px;
    top: 24px;
    box-shadow: 0 0 12px rgba(52, 212, 255, 0.5);
}

.chat-shell {
    width: min(100%, 1100px);
    margin: 0 auto 0.5rem;
    padding: 0.55rem 0.6rem 0.55rem 1rem;
    border-radius: 18px;
    border: 1px solid rgba(141, 92, 246, 0.55);
    background: rgba(255, 255, 255, 0.7);
    box-shadow: 0 0 18px rgba(141, 92, 246, 0.08);
}

[data-testid="stChatInput"] {
    border-radius: 18px !important;
    border: 1px solid rgba(141, 92, 246, 0.45) !important;
    background: rgba(255, 255, 255, 0.82) !important;
    box-shadow: inset 0 0 0 1px rgba(255,255,255,0.02), 0 0 10px rgba(141, 92, 246, 0.08) !important;
}

[data-testid="stChatInput"] textarea {
    min-height: 58px !important;
    font-size: 1.08rem !important;
    background: transparent !important;
    border: none !important;
    color: #1f2937 !important;
}

[data-testid="stChatInput"] button {
    background: linear-gradient(135deg, rgba(141, 92, 246, 1), rgba(80, 110, 255, 1)) !important;
    border: none !important;
    border-radius: 14px !important;
    min-width: 44px !important;
    min-height: 44px !important;
    box-shadow: 0 0 14px rgba(141, 92, 246, 0.4) !important;
}

.user-message {
    background: linear-gradient(135deg, rgba(141, 92, 246, 0.18), rgba(34, 211, 238, 0.1));
    color: var(--rp-text);
    padding: 14px 16px;
    border-radius: 16px;
    margin: 10px 0 10px auto;
    width: fit-content;
    max-width: 70%;
    text-align: left;
    border: 1px solid rgba(168, 85, 247, 0.42);
    box-shadow: 0 0 18px rgba(168, 85, 247, 0.1), 0 10px 24px rgba(15, 23, 42, 0.45);
    line-height: 1.55;
}

.bot-message {
    background: linear-gradient(135deg, rgba(12, 17, 31, 0.94), rgba(18, 24, 39, 0.9));
    color: var(--rp-text);
    padding: 14px 16px;
    border-radius: 16px;
    margin: 10px auto 10px 0;
    width: fit-content;
    max-width: 75%;
    text-align: left;
    border: 1px solid rgba(52, 212, 255, 0.28);
    box-shadow: 0 0 16px rgba(52, 212, 255, 0.08), 0 12px 24px rgba(15, 23, 42, 0.4);
    line-height: 1.6;
}

.source-box {
    background: linear-gradient(135deg, rgba(17, 24, 39, 0.92), rgba(19, 35, 46, 0.8));
    color: var(--rp-muted);
    padding: 10px 12px;
    border-radius: 12px;
    font-size: 13px;
    margin-top: 8px;
    border: 1px solid rgba(244, 114, 182, 0.25);
    max-width: 75%;
    line-height: 1.45;
}

.user-message b,
.bot-message b,
.source-box b {
    color: var(--rp-text);
}

[data-testid="stAlert"] {
    background-color: var(--rp-panel) !important;
    color: var(--rp-text) !important;
    border: 1px solid var(--rp-border) !important;
}

[data-testid="stAlert"] div,
[data-testid="stAlert"] p {
    color: var(--rp-text) !important;
}

hr {
    border-color: var(--rp-border) !important;
}

@media (max-width: 720px) {
    .main .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }

    .hero-visual {
        width: 100%;
        height: 210px;
    }

    .hero-book {
        width: 240px;
        height: 110px;
    }

    .hero-pdf {
        width: 84px;
        height: 84px;
        font-size: 1.4rem;
    }

    .user-message,
    .bot-message,
    .source-box {
        max-width: 100%;
    }
}
</style>
"""

user_template = """
<div class="user-message">
    <b>You:</b><br>
    {{MSG}}
</div>
"""

bot_template = """
<div class="bot-message">
    <b>Assistant:</b><br>
    {{MSG}}
</div>
"""

source_template = """
<div class="source-box">
    <b>Sources:</b><br>
    {{SOURCES}}
</div>
"""