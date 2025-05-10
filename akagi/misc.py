MJAI_TILE_TO_UNICODE: dict[str, str] = {
    "1m": "🀇 ", "2m": "🀈 ", "3m": "🀉 ", "4m": "🀊 ", "5m": "🀋 ", "6m": "🀌 ", "7m": "🀍 ", "8m": "🀎 ", "9m": "🀏 ",
    "1p": "🀙 ", "2p": "🀚 ", "3p": "🀛 ", "4p": "🀜 ", "5p": "🀝 ", "6p": "🀞 ", "7p": "🀟 ", "8p": "🀠 ", "9p": "🀡 ",
    "1s": "🀐 ", "2s": "🀑 ", "3s": "🀒 ", "4s": "🀓 ", "5s": "🀔 ", "6s": "🀕 ", "7s": "🀖 ", "8s": "🀗 ", "9s": "🀘 ",
    "E": "🀀 ", "S": "🀁 ", "W": "🀂 ", "N": "🀃 ",
    "P": "🀆 ", "F": "🀅 ", "C": "🀄︎", 
    # 中 here doesn't have a space after it, this is because the font of 🀄︎ is a 2 blocks wide character in terminal.
    "5mr": "🀋 ", "5pr": "🀝 ", "5sr": "🀔 ",
}
MJAI_TILE_TO_UNICODE_NOSPACE: dict[str, str] = {
    "1m": "🀇", "2m": "🀈", "3m": "🀉", "4m": "🀊", "5m": "🀋", "6m": "🀌", "7m": "🀍", "8m": "🀎", "9m": "🀏",
    "1p": "🀙", "2p": "🀚", "3p": "🀛", "4p": "🀜", "5p": "🀝", "6p": "🀞", "7p": "🀟", "8p": "🀠", "9p": "🀡",
    "1s": "🀐", "2s": "🀑", "3s": "🀒", "4s": "🀓", "5s": "🀔", "6s": "🀕", "7s": "🀖", "8s": "🀗", "9s": "🀘",
    "E":  "🀀", "S":  "🀁", "W":  "🀂", "N":  "🀃",
    "P":  "🀆",  "F": "🀅",  "C": "🀄︎", 
    "5mr":"🀋", "5pr":"🀝", "5sr":"🀔",
}
TILE_2_UNICODE_ART_RICH = {
    '5mr': 
    """[bold $text-error]╭──────╮
│ .伍  │
│      │
│  萬  │
╰──────╯""",
    '1m': 
    """[bold]╭──────╮
│  一  │
│      │
│  [$text-error]萬[/$text-error]  │
╰──────╯""",
    '2m': 
    """[bold]╭──────╮
│  二  │
│      │
│  [$text-error]萬[/$text-error]  │
╰──────╯""",
    '3m': 
    """[bold]╭──────╮
│  三  │
│      │
│  [$text-error]萬[/$text-error]  │
╰──────╯""",
    '4m': 
    """[bold]╭──────╮
│  四  │
│      │
│  [$text-error]萬[/$text-error]  │
╰──────╯""",
    '5m': 
    """[bold]╭──────╮
│  伍  │
│      │
│  [$text-error]萬[/$text-error]  │
╰──────╯""",
    '6m': 
    """[bold]╭──────╮
│  六  │
│      │
│  [$text-error]萬[/$text-error]  │
╰──────╯""",
    '7m': 
    """[bold]╭──────╮
│  七  │
│      │
│  [$text-error]萬[/$text-error]  │
╰──────╯""",
    '8m': 
    """[bold]╭──────╮
│  八  │
│      │
│  [$text-error]萬[/$text-error]  │
╰──────╯""",
    '9m': 
    """[bold]╭──────╮
│  九  │
│      │
│  [$text-error]萬[/$text-error]  │
╰──────╯""",
    '5pr': 
    """[bold $text-error]╭─────╮
│ ● ● │
│ .●  │
│ ● ● │
╰─────╯""",
    '1p': 
    """[bold]╭─────╮
│     │
│  ●  │
│     │
╰─────╯""",
    '2p': 
    """[bold]╭─────╮
│  ●  │
│     │
│  ●  │
╰─────╯""",
    '3p': 
    """[bold]╭─────╮
│ ●   │
│  [$text-error]●[/$text-error]  │
│   ● │
╰─────╯""",
    '4p': 
    """[bold]╭─────╮
│ ● ● │
│     │
│ ● ● │
╰─────╯""",
    '5p': 
    """[bold]╭─────╮
│ ● ● │
│  [$text-error]●[/$text-error]  │
│ ● ● │
╰─────╯""",
    '6p': 
    """[bold]╭─────╮
│ ● ● │
│ [$text-error]● ●[/$text-error] │
│ [$text-error]● ●[/$text-error] │
╰─────╯""",
    '7p': 
    """[bold]╭─────╮
│● ● ●│
│ [$text-error]● ●[/$text-error] │
│ [$text-error]● ●[/$text-error] │
╰─────╯""",
    '8p': 
    """[bold]╭─────╮
│ 8 8 │
│ ● ● │
│ ● ● │
╰─────╯""",
    '9p': 
    """[bold]╭─────╮
│● ● ●│
│[$text-error]● ● ●[/$text-error]│
│● ● ●│
╰─────╯""",
    '5sr': 
    """[bold $text-error]╭─────╮
│ I.I │
│  I  │
│ I I │
╰─────╯""",
    '1s': 
    """[bold]╭─────╮
│  [$text-success]╦[/$text-success]  │
│  [$text-success]║[/$text-success]  │
│  [$text-success]╩[/$text-success]  │
╰─────╯""",
    '2s': 
    """[bold]╭─────╮
│  [$text-success]I[/$text-success]  │
│     │
│  [$text-success]I[/$text-success]  │
╰─────╯""",
    '3s': 
    """[bold]╭─────╮
│  [$text-success]I[/$text-success]  │
│     │
│ [$text-success]I I[/$text-success] │
╰─────╯""",
    '4s': 
    """[bold]╭─────╮
│ [$text-success]I I[/$text-success] │
│     │
│ [$text-success]I I[/$text-success] │
╰─────╯""",
    '5s': 
    """[bold]╭─────╮
│ [$text-success]I I[/$text-success] │
│  [$text-error]I[/$text-error]  │
│ [$text-success]I I[/$text-success] │
╰─────╯""",
    '6s': 
    """[bold]╭─────╮
│ [$text-success]I I[/$text-success] │
│ [$text-success]I I[/$text-success] │
│ [$text-success]I I[/$text-success] │
╰─────╯""",
    '7s': 
    """[bold]╭─────╮
│  [$text-error]I[/$text-error]  │
│[$text-success]I I I[/$text-success]│
│[$text-success]I I I[/$text-success]│
╰─────╯""",
    '8s': 
    """[bold]╭─────╮
│[$text-success]│╱ ╲│[/$text-success]│
│     │
│[$text-success]│╲ ╱│[/$text-success]│
╰─────╯""",
    '9s': 
    """[bold]╭─────╮
│[$text-success]I[/$text-success] [$text-error]I[/$text-error] [$text-success]I[/$text-success]│
│[$text-success]I[/$text-success] [$text-error]I[/$text-error] [$text-success]I[/$text-success]│
│[$text-success]I[/$text-success] [$text-error]I[/$text-error] [$text-success]I[/$text-success]│
╰─────╯""",
    'E': 
    """[bold]╭──────╮
│      │
│  東  │
│      │
╰──────╯""",
    'S': 
    """[bold]╭──────╮
│      │
│  南  │
│      │
╰──────╯""",
    'W': 
    """[bold]╭──────╮
│      │
│  西  │
│      │
╰──────╯""",
    'N': 
    """[bold]╭──────╮
│      │
│  北  │
│      │
╰──────╯""",
    'P': 
    """[bold]╭──────╮
│      │
│      │
│      │
╰──────╯""",
    'F': 
    """[bold]╭──────╮
│      │
│  [$text-success]發[/$text-success]  │
│      │
╰──────╯""",
    'C': 
    """[bold]╭──────╮
│      │
│  [$text-error]中[/$text-error]  │
│      │
╰──────╯""",
    '?': 
#     """[bold]╭─────╮
# │ ┏━┓ │
# │  ┏┛ │
# │  ●  │
# ╰─────╯""",
    """[bold]       
       
       
       
       """,
}

VERTICAL_RULE = """║
║
║
║
║"""

EMPTY_VERTICAL_RULE = """ 
 
 
 
 """
# EMPTY_VERTICAL_RULE = """.
# .
# .
# .
# ."""

from textual.color import Color
from textual.theme import Theme as TextualTheme

## Keep Galaxy theme (deep space-inspired theme with rich purples and blues)
galaxy_primary = Color.parse("#BD93F9")  # Vibrant purple
galaxy_secondary = Color.parse("#8BE9FD")  # Bright cyan
galaxy_warning = Color.parse("#FFB86C")  # Soft orange
galaxy_error = Color.parse("#FF5555")  # Bright red
galaxy_success = Color.parse("#50FA7B")  # Bright green
galaxy_accent = Color.parse("#FF79C6")  # Pink
galaxy_background = Color.parse("#282A36")  # Dark background
galaxy_surface = Color.parse("#383A59")  # Slightly lighter surface
galaxy_panel = Color.parse("#44475A")  # Panel color

## Keep Cyberpunk theme (neon on dark with high contrast)
cyberpunk_primary = Color.parse("#00F6FF")  # Bright cyan
cyberpunk_secondary = Color.parse("#BD00FF")  # Neon purple
cyberpunk_warning = Color.parse("#FFFC00")  # Bright yellow
cyberpunk_error = Color.parse("#FF3677")  # Hot pink
cyberpunk_success = Color.parse("#00FF9F")  # Neon green
cyberpunk_accent = Color.parse("#FF4DFD")  # Magenta
cyberpunk_background = Color.parse("#0A001A")  # Very dark purple
cyberpunk_surface = Color.parse("#150029")  # Dark purple
cyberpunk_panel = Color.parse("#200A33")  # Medium dark purple

## Add Noctura Contrast (Modern & Vibrant)
noctura_primary = Color.parse("#00A3FF")  # Vibrant Cyan
noctura_secondary = Color.parse("#FF8C00")  # Bright Orange
noctura_warning = Color.parse("#FFA500")  # Orange
noctura_error = Color.parse("#FF1744")  # Bright Red
noctura_success = Color.parse("#00C853")  # Lime Green
noctura_accent = Color.parse("#9C27B0")  # Deep Purple
noctura_background = Color.parse("#121212")  # Very Dark Gray
noctura_surface = Color.parse("#1E1E1E")  # Deep Gray
noctura_panel = Color.parse("#252525")  # Lighter Gray

## Add Cyber Night (Futuristic & Neon)
cybernight_primary = Color.parse("#0FF0FC")  # Neon Cyan
cybernight_secondary = Color.parse("#FF007A")  # Bright Pink
cybernight_warning = Color.parse("#FFB400")  # Neon Yellow
cybernight_error = Color.parse("#FF1744")  # Bright Red
cybernight_success = Color.parse("#39FF14")  # Electric Green
cybernight_accent = Color.parse("#892CDC")  # Vibrant Purple
cybernight_background = Color.parse("#0A0A0A")  # Almost Black
cybernight_surface = Color.parse("#151515")  # Dark Gray
cybernight_panel = Color.parse("#1B1B1B")  # Slightly lighter gray

## Add Midnight Rust (Muted & Professional)
midnight_rust_primary = Color.parse("#D97706")  # Deep Amber
midnight_rust_secondary = Color.parse("#BB2525")  # Rust Red
midnight_rust_warning = Color.parse("#F59E0B")  # Warm Orange
midnight_rust_error = Color.parse("#DC2626")  # Deep Red
midnight_rust_success = Color.parse("#22C55E")  # Muted Green
midnight_rust_accent = Color.parse("#8B5CF6")  # Soft Purple
midnight_rust_background = Color.parse("#181818")  # Charcoal Black
midnight_rust_surface = Color.parse("#222222")  # Dark Gray
midnight_rust_panel = Color.parse("#292929")  # Slightly lighter gray

## Add Eclipse Void (Minimal & Sleek)
eclipse_void_primary = Color.parse("#2196F3")  # Bright Blue
eclipse_void_secondary = Color.parse("#03DAC6")  # Teal
eclipse_void_warning = Color.parse("#FFB300")  # Golden Yellow
eclipse_void_error = Color.parse("#D32F2F")  # Crimson
eclipse_void_success = Color.parse("#4CAF50")  # Leaf Green
eclipse_void_accent = Color.parse("#8E24AA")  # Rich Purple
eclipse_void_background = Color.parse("#121212")  # Deep Black
eclipse_void_surface = Color.parse("#1A1A1A")  # Charcoal Gray
eclipse_void_panel = Color.parse("#252525")  # Lighter Gray

## Add Inferno Shadow (Fiery & Dramatic)
inferno_primary = Color.parse("#FF4500")  # Bright Orange
inferno_secondary = Color.parse("#FFD700")  # Gold
inferno_warning = Color.parse("#FFA500")  # Deep Orange
inferno_error = Color.parse("#FF1744")  # Blood Red
inferno_success = Color.parse("#66BB6A")  # Soft Green
inferno_accent = Color.parse("#D10000")  # Dark Red
inferno_background = Color.parse("#0A0A0A")  # Pure Black
inferno_surface = Color.parse("#161616")  # Charcoal Gray
inferno_panel = Color.parse("#222222")  # Slightly lighter gray

## Add Void Synthwave (Retro & Vibrant)
synthwave_primary = Color.parse("#FF007A")  # Neon Pink
synthwave_secondary = Color.parse("#5D00FF")  # Electric Purple
synthwave_warning = Color.parse("#FFC107")  # Golden Yellow
synthwave_error = Color.parse("#FF1744")  # Bright Red
synthwave_success = Color.parse("#00FF87")  # Neon Green
synthwave_accent = Color.parse("#00E5FF")  # Cyan
synthwave_background = Color.parse("#080808")  # Almost Black
synthwave_surface = Color.parse("#121212")  # Dark Gray
synthwave_panel = Color.parse("#1E1E1E")  # Slightly lighter gray

## Add Obsidian Frost (Cool & Icy)
obsidian_primary = Color.parse("#00BFFF")  # Deep Sky Blue
obsidian_secondary = Color.parse("#0077B6")  # Ocean Blue
obsidian_warning = Color.parse("#FBC02D")  # Light Gold
obsidian_error = Color.parse("#EF5350")  # Muted Red
obsidian_success = Color.parse("#81C784")  # Soft Green
obsidian_accent = Color.parse("#90CAF9")  # Frost Blue
obsidian_background = Color.parse("#0B0C10")  # Midnight Black
obsidian_surface = Color.parse("#1F2833")  # Dark Gray
obsidian_panel = Color.parse("#293845")  # Slightly lighter gray

ADDITIONAL_THEMES: dict[str, TextualTheme] = {
    "galaxy": TextualTheme(
        name="galaxy",
        primary="#C45AFF",
        secondary="#a684e8",
        warning="#FFD700",
        error="#FF4500",
        success="#00FA9A",
        accent="#FF69B4",
        background="#0F0F1F",
        surface="#1E1E3F",
        panel="#2D2B55",
        dark=True,
        variables={
            "input-cursor-background": "#C45AFF",
            "footer-background": "transparent",
        },
    ),
    "nebula": TextualTheme(
        name="nebula",
        primary="#4A9CFF",
        secondary="#66D9EF",
        warning="#FFB454",
        error="#FF5555",
        success="#50FA7B",
        accent="#FF79C6",
        surface="#193549",
        panel="#1F4662",
        background="#0D2137",
        dark=True,
        variables={
            "input-selection-background": "#4A9CFF 35%",
        },
    ),
    "sunset": TextualTheme(
        name="sunset",
        primary="#FF7E5F",
        secondary="#FEB47B",
        warning="#FFD93D",
        error="#FF5757",
        success="#98D8AA",
        accent="#B983FF",
        background="#2B2139",
        surface="#362C47",
        panel="#413555",
        dark=True,
        variables={
            "input-cursor-background": "#FF7E5F",
            "input-selection-background": "#FF7E5F 35%",
            "footer-background": "transparent",
            "button-color-foreground": "#2B2139",
            "method-get": "#FF7E5F",
        },
    ),
    "aurora": TextualTheme(
        name="aurora",
        primary="#45FFB3",
        secondary="#A1FCDF",
        accent="#DF7BFF",
        warning="#FFE156",
        error="#FF6B6B",
        success="#64FFDA",
        background="#0A1A2F",
        surface="#142942",
        panel="#1E3655",
        dark=True,
        variables={
            "input-cursor-background": "#45FFB3",
            "input-selection-background": "#45FFB3 35%",
            "footer-background": "transparent",
            "button-color-foreground": "#0A1A2F",
            "method-post": "#DF7BFF",
        },
    ),
    "nautilus": TextualTheme(
        name="nautilus",
        primary="#0077BE",
        secondary="#20B2AA",
        warning="#FFD700",
        error="#FF6347",
        success="#32CD32",
        accent="#FF8C00",
        background="#001F3F",
        surface="#003366",
        panel="#005A8C",
        dark=True,
    ),
    "cobalt": TextualTheme(
        name="cobalt",
        primary="#334D5C",
        secondary="#66B2FF",
        warning="#FFAA22",
        error="#E63946",
        success="#4CAF50",
        accent="#D94E64",
        surface="#27343B",
        panel="#2D3E46",
        background="#1F262A",
        dark=True,
        variables={
            "input-selection-background": "#4A9CFF 35%",
        },
    ),
    "twilight": TextualTheme(
        name="twilight",
        primary="#367588",
        secondary="#5F9EA0",
        warning="#FFD700",
        error="#FF6347",
        success="#00FA9A",
        accent="#FF7F50",
        background="#191970",
        surface="#3B3B6D",
        panel="#4C516D",
        dark=True,
    ),
    "hacker": TextualTheme(
        name="hacker",
        primary="#00FF00",
        secondary="#3A9F3A",
        warning="#00FF66",
        error="#FF0000",
        success="#00DD00",
        accent="#00FF33",
        background="#000000",
        surface="#0A0A0A",
        panel="#111111",
        dark=True,
        variables={
            "method-get": "#00FF00",
            "method-post": "#00DD00",
            "method-put": "#00BB00",
            "method-delete": "#FF0000",
            "method-patch": "#00FF33",
            "method-options": "#3A9F3A",
            "method-head": "#00FF66",
        },
    ),
    "manuscript": TextualTheme(
        name="manuscript",
        primary="#2C4251",  # Ink blue
        secondary="#6B4423",  # Aged leather brown
        accent="#8B4513",  # Rich leather accent
        warning="#B4846C",  # Faded sepia
        error="#A94442",  # Muted red ink
        success="#2D5A27",  # Library green
        background="#F5F1E9",  # Aged paper
        surface="#EBE6D9",  # Textured paper
        panel="#E0DAC8",  # Parchment
        dark=False,
        variables={
            "input-cursor-background": "#2C4251",
            "input-selection-background": "#2C4251 25%",
            "footer-background": "#2C4251",
            "footer-key-foreground": "#F5F1E9",
            "footer-description-foreground": "#F5F1E9",
            "button-color-foreground": "#F5F1E9",
            "method-get": "#2C4251",  # Ink blue
            "method-post": "#2D5A27",  # Library green
            "method-put": "#6B4423",  # Leather brown
            "method-delete": "#A94442",  # Red ink
            "method-patch": "#8B4513",  # Rich leather
            "method-options": "#4A4A4A",  # Dark gray ink
            "method-head": "#5C5C5C",  # Gray ink
        },
    ),
    "cynosure": TextualTheme(
        name="cynosure",
        primary="#e8e1c1",
        secondary="#ff0000",
        accent="#ff0000",
        foreground="#beb986",
        background="#112835",
        success="#beb986",
        warning="#EBCB8B",
        error="#ff0000",
        surface="#3B4252",
        panel="#434C5E",
        dark=True,
        variables={
            "block-cursor-text-style": "none",
            "footer-key-foreground": "#88C0D0",
            "input-selection-background": "#81a1c1 35%",
        },
    ),
    "downtown": TextualTheme(
        name="downtown",
        primary="#e41d59",
        secondary="#f76120",
        accent="#ff6947",
        foreground="#eacbd5",
        background="#29232e",
        success="#b7c664",
        warning="#cd854c",
        error="#cd5a4c",
        surface="#201b24",
        panel="#1a161d",
        dark=True,
	),
    "arctic": TextualTheme(
        name="arctic",
        primary="#88C0D0",
        secondary="#81A1C1",
        accent="#B48EAD",
        foreground="#D8DEE9",
        background="#2E3440",
        success="#A3BE8C",
        warning="#EBCB8B",
        error="#BF616A",
        surface="#3B4252",
        panel="#434C5E",
        dark=True,
        variables={
            "block-cursor-text-style": "none",
            "footer-key-foreground": "#88C0D0",
            "input-selection-background": "#81a1c1 35%",
        },
    ),
    "harlequin": TextualTheme(
        name="harlequin",
        primary="#FEFFAC",
        secondary="#45FFCA",
        warning="#FEFFAC",
        error="#FFB6D9",
        success="#45FFCA",
        accent="#FEFFAC",
        foreground="#DDDDDD",
        background="#0C0C0C",
        surface="#0C0C0C",
        panel="#555555",
        dark=True,
    ),
	"moulti-dark": TextualTheme(
		name="moulti-dark",
		primary="#0178D4",
		secondary="#004578",
		warning="#ffa62b",
		error="#ba3c5b",
		success="#4ebf71",
		accent="#ffa62b",
		foreground="#e0e0e0", #
		background="#1e1e1e", #
		surface="#121212",    #
		panel="#24292f",      #
		boost=None,
		dark=True,
		luminosity_spread = 0.15,
		text_alpha = 0.95,
		variables={
			"footer-key-foreground": "#ffffff",
		},
	),
	"moulti-light": TextualTheme(
		name="moulti-light",
		primary="#0178D4",
		secondary="#004578",
		warning="#ffa62b",
		error="#ba3c5b",
		success="#4ebf71",
		accent="#ffa62b",
		foreground="#0a0a0a", #
		background="#f5f5f5", #
		surface="#efefef",    #
		panel="#dce3e8",      #
		boost=None,
		dark=False,
		luminosity_spread = 0.15,
		text_alpha = 0.95,
		variables={
			"footer-key-foreground": "#ffffff",
		},
	),
    "IBM 3270": TextualTheme(
        name="IBM 3270",
        primary="#00feff",
        secondary="#17f9e1",
        accent="#ff0000",
        foreground="#f3ebdb",
        background="#000000",
        success="#0efd03",
        warning="#f5ff30",
        error="#ff0000",
        surface="#000000",
        panel="#0efd03",
        dark=True,
        variables={
            "block-cursor-text-style": "none",
            "footer-key-foreground": "#88C0D0",
            "input-selection-background": "#81a1c1 35%",
            "border": "#17f9e1",
            "border-blurred": "#17f9e1",
            "footer-foreground": "#000000",
            "footer-key-foreground": "#000000",
            "footer-description-foreground": "#000000",
        },
    ),
    "cassette-dark": TextualTheme(
        name="cassette-dark",
        primary="#b1b329",       
        secondary="#008001",     
        accent="#9b50b7",        
        background="#002f33",    
        foreground="#FAF0E6",    
        success="#008001",       
        warning="#FFFF00",      
        error="#FF0000",        
        surface="#262626",      
        panel="#333333",        
        dark=True,
        variables={
            "border": "#b1b329 60%",  
            "scrollbar": "#002f33",   
            "button-background": "#00FF00",
            "button-color-foreground": "#1A1A1A",
            "footer-key-foreground": "#9b50b7",
            "input-cursor-background":"#FFFF00",
            "datatable--header-cursor":"#FFFF00",
            "button-focus-text-style": "bold",
        }
    ),
    "cassette-walkman": TextualTheme(
        name="cassette-walkman",
        primary="#43748f",       
        secondary="#6e92a6",      
        accent="#ef8e04",        
        background="#e7e5e6",    
        foreground="#353530",     
        success="#43748f",       
        warning="#DAA520",       
        error="#ef8e04",        
        surface="#43748f",       
        panel="#d6d6d6",         
        dark=False,
        variables={
            "border": "#6e92a6 60%",  
            "scrollbar": "#d6d6d6",  
            "button-color-foreground": "#313a44",
            "footer-key-foreground": "#ef8e04",
            "button-focus-text-style": "bold",
        }
    ),
    "cassette-light": TextualTheme(
        name="cassette-light",
        primary="#F4A460",       
        secondary="#C0C0C0",      
        accent="#f24d11",        
        background="#fcf2d4",    
        foreground="#333333",     
        success="#00FFFF",       
        warning="#DAA520",       
        error="#FF4500",        
        surface="#FFFFF0",       
        panel="#FFFFF0",         
        dark=False,
        variables={
            "border": "#ec6809 60%",  # dodgerblue
            "scrollbar": "#fcf2d4",   # silver
            "button-background": "#ec6809",
            "button-color-foreground": "#333333",
            "footer-key-foreground": "#ec6809",
            "button-focus-text-style": "bold",
        }
    ),
    "github-dark": TextualTheme(
        name="github-dark",
        primary="#68A2D7",
        secondary="#81A1C1",
        accent="#B48EAD",
        foreground="#CDD9E5",
        background="#1C2128",
        success="#A3BE8C",
        warning="#EBCB8B",
        error="#BF616A",
        surface="#22272E",
        panel="#434C5E",
        dark=True,
        variables={
            "block-cursor-text-style": "none",
            "footer-key-foreground": "#88C0D0",
            "input-selection-background": "#81a1c1 35%",
        },
    ),
    "chezmoi-mousse-dark": TextualTheme(
        name="chezmoi-mousse-dark",
        dark=True,
        accent="#F187FB",
        background="#000000",
        error="#ba3c5b",  # textual dark
        foreground="#DEDAE1",
        primary="#0178D4",  # textual dark
        secondary="#004578",  # textual dark
        success="#4EBF71",  # textual dark
        warning="#ffa62b",  # textual dark
    ),
    "flexi": TextualTheme(
        name="flexi",
        primary="#38bdf8",
        secondary="#0891b2",
        accent="#0d9488",
        foreground="#D8DEE9",
        background="#1d1d1d",
        success="#A3BE8C",
        warning="#EBCB8B",
        error="#BF616A",
        surface="#3B4252",
        panel="#434C5E",
        dark=True,
        variables={
            "block-cursor-text-style": "none",
            "footer-key-foreground": "#88C0D0",
            "input-selection-background": "#0d9488 35%",
        },
    ),
    "galaxy": TextualTheme(
        name="galaxy",
        primary=galaxy_primary.hex,
        secondary=galaxy_secondary.hex,
        warning=galaxy_warning.hex,
        error=galaxy_error.hex,
        success=galaxy_success.hex,
        accent=galaxy_accent.hex,
        background=galaxy_background.hex,
        surface=galaxy_surface.hex,
        panel=galaxy_panel.hex,
        dark=True,
        variables={
            "input-cursor-background": galaxy_primary.hex,
            "input-selection-background": f"{galaxy_primary.hex} 35%",
            "footer-background": "transparent",
            "border-color": f"{galaxy_primary.hex} 30%",
            "text": "#F8F8F2",  # Bright text
            "text-muted": "#BFBFBF",  # Muted text
            "primary-background": "#373844",  # Slightly lighter than surface
            "primary-darken-1": galaxy_primary.darken(0.1).hex,
            "primary-darken-2": galaxy_primary.darken(0.2).hex,
            "selection": f"{galaxy_primary.hex} 30%",
        },
    ),
    "cyberpunk": TextualTheme(
        name="cyberpunk",
        primary=cyberpunk_primary.hex,
        secondary=cyberpunk_secondary.hex,
        warning=cyberpunk_warning.hex,
        error=cyberpunk_error.hex,
        success=cyberpunk_success.hex,
        accent=cyberpunk_accent.hex,
        background=cyberpunk_background.hex,
        surface=cyberpunk_surface.hex,
        panel=cyberpunk_panel.hex,
        dark=True,
        variables={
            "input-cursor-background": cyberpunk_primary.hex,
            "input-selection-background": f"{cyberpunk_primary.hex} 35%",
            "footer-background": "transparent",
            "border-color": f"{cyberpunk_primary.hex} 30%",
            "text": "#EEFFFF",  # Bright cyan-white
            "text-muted": "#A2D6E9",  # Muted cyan
            "primary-background": "#1E0E30",  # Slightly lighter background
            "primary-darken-1": cyberpunk_primary.darken(0.1).hex,
            "primary-darken-2": cyberpunk_primary.darken(0.2).hex,
            "selection": f"{cyberpunk_secondary.hex} 50%",
        },
    ),
    # New theme: Noctura Contrast
    "noctura": TextualTheme(
        name="noctura",
        primary=noctura_primary.hex,
        secondary=noctura_secondary.hex,
        warning=noctura_warning.hex,
        error=noctura_error.hex,
        success=noctura_success.hex,
        accent=noctura_accent.hex,
        background=noctura_background.hex,
        surface=noctura_surface.hex,
        panel=noctura_panel.hex,
        dark=True,
        variables={
            "input-cursor-background": noctura_primary.hex,
            "input-selection-background": f"{noctura_primary.hex} 35%",
            "footer-background": "transparent",
            "border-color": f"{noctura_primary.hex} 30%",
            "text": "#EAEAEA",  # Near-white text
            "text-muted": "#ABABAB",  # Muted white
            "primary-background": "#2A2A2A",  # Slightly lighter than surface
            "primary-darken-1": noctura_primary.darken(0.1).hex,
            "primary-darken-2": noctura_primary.darken(0.2).hex,
            "selection": f"{noctura_primary.hex} 30%",
        },
    ),
    # New theme: Cyber Night
    "cybernight": TextualTheme(
        name="cybernight",
        primary=cybernight_primary.hex,
        secondary=cybernight_secondary.hex,
        warning=cybernight_warning.hex,
        error=cybernight_error.hex,
        success=cybernight_success.hex,
        accent=cybernight_accent.hex,
        background=cybernight_background.hex,
        surface=cybernight_surface.hex,
        panel=cybernight_panel.hex,
        dark=True,
        variables={
            "input-cursor-background": cybernight_primary.hex,
            "input-selection-background": f"{cybernight_primary.hex} 35%",
            "footer-background": "transparent",
            "border-color": f"{cybernight_primary.hex} 30%",
            "text": "#F5F5F5",  # Soft white
            "text-muted": "#A0A0A0",  # Medium gray
            "primary-background": "#1F1F1F",  # Slightly lighter than surface
            "primary-darken-1": cybernight_primary.darken(0.1).hex,
            "primary-darken-2": cybernight_primary.darken(0.2).hex,
            "selection": f"{cybernight_accent.hex} 40%",
        },
    ),
    # New theme: Midnight Rust
    "midnight_rust": TextualTheme(
        name="midnight_rust",
        primary=midnight_rust_primary.hex,
        secondary=midnight_rust_secondary.hex,
        warning=midnight_rust_warning.hex,
        error=midnight_rust_error.hex,
        success=midnight_rust_success.hex,
        accent=midnight_rust_accent.hex,
        background=midnight_rust_background.hex,
        surface=midnight_rust_surface.hex,
        panel=midnight_rust_panel.hex,
        dark=True,
        variables={
            "input-cursor-background": midnight_rust_primary.hex,
            "input-selection-background": f"{midnight_rust_primary.hex} 35%",
            "footer-background": "transparent",
            "border-color": f"{midnight_rust_primary.hex} 30%",
            "text": "#E4E4E4",  # Soft white
            "text-muted": "#AAAAAA",  # Light gray
            "primary-background": "#262626",  # Slightly lighter than surface
            "primary-darken-1": midnight_rust_primary.darken(0.1).hex,
            "primary-darken-2": midnight_rust_primary.darken(0.2).hex,
            "selection": f"{midnight_rust_primary.hex} 30%",
        },
    ),
    # New theme: Eclipse Void
    "eclipse": TextualTheme(
        name="eclipse",
        primary=eclipse_void_primary.hex,
        secondary=eclipse_void_secondary.hex,
        warning=eclipse_void_warning.hex,
        error=eclipse_void_error.hex,
        success=eclipse_void_success.hex,
        accent=eclipse_void_accent.hex,
        background=eclipse_void_background.hex,
        surface=eclipse_void_surface.hex,
        panel=eclipse_void_panel.hex,
        dark=True,
        variables={
            "input-cursor-background": eclipse_void_primary.hex,
            "input-selection-background": f"{eclipse_void_primary.hex} 35%",
            "footer-background": "transparent",
            "border-color": f"{eclipse_void_primary.hex} 30%",
            "text": "#E0E0E0",  # Soft white
            "text-muted": "#A0A0A0",  # Medium gray
            "primary-background": "#202020",  # Slightly lighter than surface
            "primary-darken-1": eclipse_void_primary.darken(0.1).hex,
            "primary-darken-2": eclipse_void_primary.darken(0.2).hex,
            "selection": f"{eclipse_void_primary.hex} 30%",
        },
    ),
    # New theme: Inferno Shadow
    "inferno": TextualTheme(
        name="inferno",
        primary=inferno_primary.hex,
        secondary=inferno_secondary.hex,
        warning=inferno_warning.hex,
        error=inferno_error.hex,
        success=inferno_success.hex,
        accent=inferno_accent.hex,
        background=inferno_background.hex,
        surface=inferno_surface.hex,
        panel=inferno_panel.hex,
        dark=True,
        variables={
            "input-cursor-background": inferno_primary.hex,
            "input-selection-background": f"{inferno_primary.hex} 35%",
            "footer-background": "transparent",
            "border-color": f"{inferno_primary.hex} 30%",
            "text": "#F8F8F8",  # Soft white
            "text-muted": "#BBBBBB",  # Light gray
            "primary-background": "#1A1A1A",  # Slightly lighter than surface
            "primary-darken-1": inferno_primary.darken(0.1).hex,
            "primary-darken-2": inferno_primary.darken(0.2).hex,
            "selection": f"{inferno_secondary.hex} 30%",
            "boost": f"{inferno_primary.hex} 15%",  # Orange overlay
        },
    ),
    # New theme: Void Synthwave
    "synthwave": TextualTheme(
        name="synthwave",
        primary=synthwave_primary.hex,
        secondary=synthwave_secondary.hex,
        warning=synthwave_warning.hex,
        error=synthwave_error.hex,
        success=synthwave_success.hex,
        accent=synthwave_accent.hex,
        background=synthwave_background.hex,
        surface=synthwave_surface.hex,
        panel=synthwave_panel.hex,
        dark=True,
        variables={
            "input-cursor-background": synthwave_primary.hex,
            "input-selection-background": f"{synthwave_primary.hex} 35%",
            "footer-background": "transparent",
            "border-color": f"{synthwave_primary.hex} 30%",
            "text": "#FFFFFF",  # Pure white
            "text-muted": "#B0B0B0",  # Medium gray
            "primary-background": "#161616",  # Slightly lighter than surface
            "primary-darken-1": synthwave_primary.darken(0.1).hex,
            "primary-darken-2": synthwave_primary.darken(0.2).hex,
            "selection": f"{synthwave_primary.hex} 30%",
            "boost": f"{synthwave_primary.hex} 20%",  # Pink overlay
        },
    ),
    # New theme: Obsidian Frost
    "obsidian": TextualTheme(
        name="obsidian",
        primary=obsidian_primary.hex,
        secondary=obsidian_secondary.hex,
        warning=obsidian_warning.hex,
        error=obsidian_error.hex,
        success=obsidian_success.hex,
        accent=obsidian_accent.hex,
        background=obsidian_background.hex,
        surface=obsidian_surface.hex,
        panel=obsidian_panel.hex,
        dark=True,
        variables={
            "input-cursor-background": obsidian_primary.hex,
            "input-selection-background": f"{obsidian_primary.hex} 35%",
            "footer-background": "transparent",
            "border-color": f"{obsidian_primary.hex} 30%",
            "text": "#E3F2FD",  # Soft ice blue
            "text-muted": "#A0C8E8",  # Muted blue
            "primary-background": "#2C3A47",  # Slightly lighter than surface
            "primary-darken-1": obsidian_primary.darken(0.1).hex,
            "primary-darken-2": obsidian_primary.darken(0.2).hex,
            "selection": f"{obsidian_primary.hex} 30%",
            "boost": f"{obsidian_primary.hex} 10%",  # Blue overlay
        },
    ),
    "advent": TextualTheme(
        name="advent",
        primary="#829a46",
        secondary="#eed1a5",
        accent="#b0261b",
        foreground="#eed1a5",
        background="#000000",
        success="#A3BE8C",
        warning="#b0261b",
        error="#BF616A",
        surface="#0e330a",
        panel="#1e431a",
        dark=True,
        variables={
            "block-cursor-text-style": "none",
            "footer-key-foreground": "#88C0D0",
            "input-selection-background": "#81a1c1 35%",
        },
    ),
    "tabla": TextualTheme(
        name="tabla",
        primary="#88C0D0",
        secondary="#91d3fe",
        accent="#91d3fe",
        foreground="#D8DEE9",
        background="#2E3440",
        success="#A3BE8C",
        warning="#EBCB8B",
        error="#BF616A",
        surface="#3B4252",
        panel="#434C5E",
        dark=True,
        variables={
            "block-cursor-text-style": "none",
            "footer-key-foreground": "#88C0D0",
            "input-selection-background": "#81a1c1 35%",
        },
    ),
    "inspect-dark": TextualTheme(
        name="inspect-dark",
        primary="#3376CD",
        secondary="#004578",
        accent="#ffa62b",
        warning="#ffa62b",
        error="#ba3c5b",
        success="#408558",
        foreground="#e0e0e0",
    ),
    "inspect-light": TextualTheme(
        name="inspect-light",
        primary="#4283CA",
        secondary="#0178D4",
        accent="#ffa62b",
        warning="#ffa62b",
        error="#ba3c5b",
        success="#54B98F",
        surface="#D8D8D8",
        panel="#DFDFDF",
        background="#F8F8F8",
        dark=False,
        variables={
            "footer-key-foreground": "#0178D4",
        },
    ),
    "default_powder": TextualTheme(
        name="default_powder",
        dark=False,
        background="#FAFAF8",
        foreground="#222222",
        primary="#486591",
        secondary="#2C4975",
        accent="#BBBBF7",
        error="#D93025",
        success="#4CAF50",
        warning="#FFA726",
        surface="#F5F5F2",
        panel="#FFFFFF",
    ),
    "default_slate": TextualTheme(
        name="default_slate",
        dark=True,
        background="#1A1C1E",
        foreground="#D8E1E6",
        primary="#4A6B8C",
        secondary="#2C4C6F",
        accent="#1A1C1E",
        error="#963B3B",
        success="#4CAF50",
        warning="#C7A850",
        surface="#22262A",
        panel="#2A2E32",
    ),
    "default_parchment": TextualTheme(
        name="default_parchment",
        dark=False,
        background="#F5ECD8",      # More yellow undertone
        foreground="#2C2826",
        primary="#A38B66",         # Warmer brown
        secondary="#8B735A",       # Warmer secondary
        accent="#FFF6E6",         # Warmer accent
        error="#963B3B",
        success="#4CAF50",
        warning="#C7A850",
        surface="#EDE4D0",        # More yellow undertone
        panel="#FFF9EA",          # Warmer panel
    ),

    "default_ivory": TextualTheme(
        name="default_ivory",
        dark=False,
        background="#F8F6F4",     # Desaturated white
        foreground="#2D2A26",
        primary="#9E958A",        # Desaturated brown
        secondary="#847E76",      # Desaturated secondary
        accent="#FFFDFC",        # Very slightly warm white
        error="#963B3B",
        success="#4CAF50",
        warning="#C7A850",
        surface="#F0EEEC",       # Desaturated surface
        panel="#FFFFFF",
    ),

    "default_graphite": TextualTheme(
        name="default_graphite",
        dark=True,
        background="#232326",
        foreground="#E0E0E2",
        primary="#667799",
        secondary="#445577",
        accent="#232326",
        error="#963B3B",
        success="#4CAF50",
        warning="#C7A850",
        surface="#2A2A2E",
        panel="#303034",
    ),

    "default_pearl": TextualTheme(
        name="default_pearl",
        dark=False,
        background="#F8F0F0",
        foreground="#2C2D30",
        primary="#90BCBF",
        secondary="#4E5B6B",
        accent="#FFF0F0",
        error="#963B3B",
        success="#4CAF50",
        warning="#C7A850",
        surface="#F0F2F4",
        panel="#FFFFFF",
    ),

    "default_obsidian": TextualTheme(
        name="default_obsidian",
        dark=True,
        background="#161618",
        foreground="#E6E6E8",
        primary="#665C7A",
        secondary="#4A4359",
        accent="#161618",
        error="#963B3B",
        success="#4CAF50",
        warning="#C7A850",
        surface="#1E1E21",
        panel="#252528",
    ),

    "default_charcoal": TextualTheme(
        name="default_charcoal",
        dark=True,
        background="#1D1F1E",
        foreground="#E2E3E3",
        primary="#6B7272",
        secondary="#4E5353",
        accent="#1D1F1E",
        error="#963B3B",
        success="#4CAF50",
        warning="#C7A850",
        surface="#252827",
        panel="#2D302F",
    ),

    "light_fire": TextualTheme(
        name="light_fire",
        dark=False,
        background="#FFFFFF",
        foreground="#B22222",
        primary="#FF4500",
        secondary="#FF0000",
        accent="#FFF0F5",
        error="#8B0000",
        success="#4CAF50",
        warning="#FFA726",
        surface="#FFFAFA",
        panel="#FFF0F5",
    ),
    "light_metal": TextualTheme(
        name="light_metal",
        dark=False,
        background="#FFFFFF",
        foreground="#696969",
        primary="#D3D3D3",
        secondary="#C0C0C0",
        accent="#E0FFFF",
        error="#FFE4E1",
        success="#4CAF50",
        warning="#FFA726",
        surface="#F0F8FF",
        panel="#E0FFFF",
    ),
    "light_earth": TextualTheme(
        name="light_earth",
        dark=False,
        background="#FFFFFF",
        foreground="#8B4513",
        primary="#CD853F",
        secondary="#D2691E",
        accent="#FFF5EE",
        error="#8B0000",
        success="#4CAF50",
        warning="#FFA726",
        surface="#FFF8DC",
        panel="#FFF5EE",
    ),
    "light_wood": TextualTheme(
        name="light_wood",
        dark=False,
        background="#F0FFF0",
        foreground="#006400",
        primary="#8FBC8F",
        secondary="#008000",
        accent="#DFFFDF",
        error="#D93025",
        success="#4CAF50",
        warning="#FFA726",
        surface="#E0FFE0",
        panel="#FFFFFF",
    ),
    "light_water": TextualTheme(
        name="light_water",
        dark=False,
        background="#FFFFFF",
        foreground="#00008B",
        primary="#00008B",
        secondary="#191970",
        accent="#ADD8E6",
        error="#FFE4E1",
        success="#4CAF50",
        warning="#FFA726",
        surface="#E0FFFF",
        panel="#ADD8E6",
    ),
    "dark_fire": TextualTheme(
        name="dark_fire",
        dark=True,
        background="#191919",
        foreground="#FFA500",
        primary="#8B0000",
        secondary="#B22222",
        accent="#191919",
        error="#8B0000",
        success="#4CAF50",
        warning="#FFA726",
        surface="#222222",
        panel="#222222",
    ),
    "dark_metal": TextualTheme(
        name="dark_metal",
        dark=True,
        background="#222222",
        foreground="#D3D3D3",
        primary="#708090",
        secondary="#696969",
        accent="#222222",
        error="#8B0000",
        success="#4CAF50",
        warning="#FFA726",
        surface="#191919",
        panel="#191919",
    ),
    "dark_earth": TextualTheme(
        name="dark_earth",
        dark=True,
        background="#191919",
        foreground="#F5DEB3",
        primary="#8B4513",
        secondary="#CD853F",
        accent="#191919",
        error="#8B0000",
        success="#4CAF50",
        warning="#FFA726",
        surface="#222222",
        panel="#222222",
    ),
    "dark_wood": TextualTheme(
        name="dark_wood",
        dark=True,
        background="#191919",
        foreground="#90EE90",  # Light green
        primary="#228B22",     # Forest green
        secondary="#006400",   # Dark green
        accent="#191919",
        error="#8B0000",
        success="#4CAF50",
        warning="#FFA726",
        surface="#222222",
        panel="#222222",
    ),
    "dark_water": TextualTheme(
        name="dark_water",
        dark=True,
        background="#191919",
        foreground="#87CEFA",
        primary="#7777EB",
        secondary="#0000CD",
        accent="#1966AB",
        error="#8B0000",
        success="#4CAF50",
        warning="#FFA726",
        surface="#222222",
        panel="#222222",
    ),
    "light_vata": TextualTheme(
        name="light_vata",
        dark=False,
        background="#FFF8E7",  # Ethereal light
        foreground="#FF4D00",  # Bright fire
        primary="#FFB366",     # Warm orange
        secondary="#FF8533",   # Deep orange
        accent="#FFE6CC",      # Soft ether
        error="#D93025",
        success="#4CAF50",
        warning="#FFA726",
        surface="#FFF2D9",
        panel="#FFFFFF",
    ),
    "dark_vata": TextualTheme(
        name="dark_vata",
        dark=True,
        background="#1A0F00",  # Dark ether
        foreground="#FF6600",  # Fire orange
        primary="#CC5200",     # Deep fire
        secondary="#FF8533",   # Bright fire
        accent="#1A0F00",
        error="#8B0000",
        success="#4CAF50",
        warning="#FFA726",
        surface="#261500",
        panel="#261500",
    ),
    "light_pitta": TextualTheme(
        name="light_pitta",
        dark=False,
        background="#FFF0E6",  # Warm light
        foreground="#0066CC",  # Water blue
        primary="#FF3300",     # Fire red
        secondary="#0099FF",   # Bright water
        accent="#E6F7FF",      # Light water
        error="#D93025",
        success="#4CAF50",
        warning="#FFA726",
        surface="#FFE6D9",
        panel="#FFFFFF",
    ),
    "dark_pitta": TextualTheme(
        name="dark_pitta",
        dark=True,
        background="#000D1A",  # Deep water
        foreground="#FF4D00",  # Fire orange
        primary="#0080FF",     # Water blue
        secondary="#FF3300",   # Fire red
        accent="#000D1A",
        error="#8B0000",
        success="#4CAF50",
        warning="#FFA726",
        surface="#001529",
        panel="#001529",
    ),
    "light_kapha": TextualTheme(
        name="light_kapha",
        dark=False,
        background="#F0FFFF",  # Air light
        foreground="#006699",  # Water blue
        primary="#99CCFF",     # Air blue
        secondary="#0099CC",   # Water blue
        accent="#E6FFFF",      # Light air
        error="#D93025",
        success="#4CAF50",
        warning="#FFA726",
        surface="#E6FFFF",
        panel="#FFFFFF",
    ),
    "dark_kapha": TextualTheme(
        name="dark_kapha",
        dark=True,
        background="#000033",  # Deep water
        foreground="#99CCFF",  # Air blue
        primary="#006699",     # Water blue
        secondary="#003366",   # Deep water
        accent="#000033",
        error="#8B0000",
        success="#4CAF50",
        warning="#FFA726",
        surface="#000047",
        panel="#000047",
    ),
    "fruit_strawberry": TextualTheme(
        name="fruit_strawberry",
        dark=False,
        background="#FFF5F5",
        foreground="#8B1D1D",
        primary="#E14343",
        secondary="#C13030",
        accent="#FFE5E5",
        error="#D93025",
        success="#4CAF50",
        warning="#FFA726",
        surface="#FFF0F0",
        panel="#FFFFFF",
    ),
    "fruit_blueberry": TextualTheme(
        name="fruit_blueberry",
        dark=True,
        background="#1A1B2E",
        foreground="#E6E7FF",
        primary="#4A4E8C",
        secondary="#363A77",
        accent="#1A1B2E",
        error="#963B3B",
        success="#4CAF50",
        warning="#C7A850",
        surface="#222438",
        panel="#2A2C42",
    ),
    "fruit_dragonfruit": TextualTheme(
        name="fruit_dragonfruit",
        dark=False,
        background="#FFF5F9",
        foreground="#4A2037",
        primary="#E875B0",
        secondary="#C45C8F",
        accent="#FFE5F2",
        error="#D93025",
        success="#4CAF50",
        warning="#FFA726",
        surface="#FFF0F5",
        panel="#FFFFFF",
    ),
    "fruit_blackberry": TextualTheme(
        name="fruit_blackberry",
        dark=True,
        background="#1A1522",
        foreground="#E6D9F2",
        primary="#614875",
        secondary="#4A3459",
        accent="#1A1522",
        error="#963B3B",
        success="#4CAF50",
        warning="#C7A850",
        surface="#221B2E",
        panel="#2A2238",
    ),
    "fruit_blood_orange": TextualTheme(
        name="fruit_blood_orange",
        dark=False,
        background="#FFF5F5",
        foreground="#8B1D1D",
        primary="#C41E3A",
        secondary="#A01830",
        accent="#FFE5E5",
        error="#D93025",
        success="#4CAF50",
        warning="#FFA726",
        surface="#FFF0F0",
        panel="#FFFFFF",
    ),
    "fruit_avocado": TextualTheme(
        name="fruit_avocado",
        dark=False,
        background="#F5FAF5",
        foreground="#2C4A2C",
        primary="#567C56",
        secondary="#445E44",
        accent="#E5FFE5",
        error="#D93025",
        success="#4CAF50",
        warning="#FFA726",
        surface="#F0FFF0",
        panel="#FFFFFF",
    ),
    "fruit_mango": TextualTheme(
        name="fruit_mango",
        dark=False,
        background="#FFF9F5",
        foreground="#8B4513",
        primary="#FF9B4D",
        secondary="#E68A44",
        accent="#FFE5D9",
        error="#D93025",
        success="#4CAF50",
        warning="#FFA726",
        surface="#FFF4F0",
        panel="#FFFFFF",
    ),
    "fruit_plum": TextualTheme(
        name="fruit_plum",
        dark=True,
        background="#1A151A",
        foreground="#E6D9E6",
        primary="#8B4B8B",
        secondary="#6E3C6E",
        accent="#1A151A",
        error="#963B3B",
        success="#4CAF50",
        warning="#C7A850",
        surface="#221B22",
        panel="#2A222A",
    ),
    "dbridges": TextualTheme(
        name="dbridges",
        primary="#d1ecff",
        secondary="#fffed3",
        accent="#9c815f",
        foreground="#444444",
        background="#ffffff",
        success="#A3BE8C",
        warning="#EBCB8B",
        error="#BF616A",
        surface="#ffffff",
        panel="#ffffff",
        dark=False,
        variables={
            "block-cursor-text-style": "none",
            "input-selection-background": "#d1ecff",
        },
    ),
    "cynosure": TextualTheme(
        name="cynosure",
        primary="#e8e1c1",
        secondary="#ff0000",
        accent="#ff0000",
        foreground="#beb986",
        background="#112835",
        success="#beb986",
        warning="#EBCB8B",
        error="#ff0000",
        surface="#3B4252",
        panel="#434C5E",
        dark=True,
        variables={
            "block-cursor-text-style": "none",
            "footer-key-foreground": "#88C0D0",
            "input-selection-background": "#81a1c1 35%",
        },
    ),
    "monokai": TextualTheme(
        name="monokai",
        primary="#F92672",  # Pink
        secondary="#66D9EF",  # Light Blue
        warning="#FD971F",  # Orange
        error="#F92672",  # Pink (same as primary for consistency)
        success="#A6E22E",  # Green
        accent="#AE81FF",  # Purple
        background="#272822",  # Dark gray-green
        surface="#3E3D32",  # Slightly lighter gray-green
        panel="#3E3D32",  # Same as surface for consistency
        dark=True,
    ),
    "retro_wave": TextualTheme(
        name="retro_wave",
        primary="#FF6EC7",  # Neon Pink
        secondary="#FFD700",  # Golden Yellow
        warning="#FFA500",  # Orange
        error="#E60000",  # Deep Red
        success="#39FF14",  # Electric Green
        accent="#8B00FF",  # Electric Purple
        dark=True,
        background="#2D1E2F",  # Dark Purple
        surface="#3B2E50",  # Muted Dark Blue
        panel="#503571",  # Deep Magenta
    ),
        "holographic": TextualTheme(
        name="holographic",
        primary="rgba(173, 216, 230, 0.7)",  # Soft Light Blue
        secondary="rgba(255, 182, 193, 0.7)",  # Light Pink
        warning="rgba(255, 215, 0, 0.7)",  # Gold
        error="rgba(255, 99, 71, 0.7)",  # Tomato Red
        success="rgba(124, 252, 0, 0.7)",  # Neon Green
        accent="rgba(186, 85, 211, 0.7)",  # Medium Orchid
        dark=False,
        background="rgba(240, 248, 255, 0.2)",  # Very Light Transparent Blue
        surface="rgba(200, 225, 255, 0.3)",  # Soft Blue Tint
        panel="rgba(175, 200, 255, 0.4)",  # Slightly Darker Blue Tint
    ),
    "transparent_night": TextualTheme(
        name="transparent_night",
        primary="rgba(100, 200, 255, 0.7)",  # Soft Cyan
        secondary="rgba(200, 150, 255, 0.7)",  # Light Purple
        warning="rgba(255, 165, 0, 0.7)",  # Orange
        error="rgba(255, 69, 0, 0.7)",  # Red-Orange
        success="rgba(50, 205, 50, 0.7)",  # Lime Green
        accent="rgba(255, 105, 180, 0.7)",  # Hot Pink
        dark=True,
        background="rgba(15, 15, 40, 0.3)",  # Deep Navy Transparency
        surface="rgba(25, 25, 50, 0.4)",  # Dark Blue Tint
        panel="rgba(45, 45, 75, 0.5)",  # Slightly Lighter Blue Tint
    ),
    "ethereal": TextualTheme(
        name="ethereal",
        primary="rgba(255, 240, 245, 0.7)",  # Lavender Blush
        secondary="rgba(221, 160, 221, 0.7)",  # Plum
        warning="rgba(255, 223, 186, 0.7)",  # Peach Puff
        error="rgba(255, 69, 96, 0.7)",  # Bright Red-Pink
        success="rgba(144, 238, 144, 0.7)",  # Light Green
        accent="rgba(135, 206, 250, 0.7)",  # Light Sky Blue
        dark=False,
        background="rgba(245, 245, 245, 0.2)",  # Ultra Soft White
        surface="rgba(225, 225, 225, 0.3)",  # Light Mist Gray
        panel="rgba(205, 205, 205, 0.4)",  # Slightly Darker Mist Gray
    ),
    "cyber_glass": TextualTheme(
        name="cyber_glass",
        primary="rgba(255, 0, 255, 0.7)",  # Neon Magenta
        secondary="rgba(0, 255, 255, 0.7)",  # Cyan Glow
        warning="rgba(255, 255, 0, 0.7)",  # Neon Yellow
        error="rgba(255, 0, 0, 0.7)",  # Bright Red
        success="rgba(0, 255, 127, 0.7)",  # Neon Green
        accent="rgba(75, 0, 130, 0.7)",  # Electric Indigo
        dark=True,
        background="rgba(10, 10, 10, 0.2)",  # Almost Black Transparency
        surface="rgba(20, 20, 20, 0.3)",  # Dark Gray Tint
        panel="rgba(40, 40, 40, 0.4)",  # Slightly Brighter Gray
    ),
    "glass-ansi": TextualTheme(
        name="glass-ansi",
        primary="ansi_bright_white",
        secondary="ansi_bright_cyan",
        warning="ansi_yellow",
        error="ansi_red",
        success="ansi_green",
        accent="ansi_bright_blue",
        foreground="ansi_default",  # Uses terminal's default text color
        background="ansi_default",  # Transparent effect
        surface="ansi_default",
        panel="ansi_default",
        boost="ansi_default",
        dark=False,
        variables={
            "block-cursor-text-style": "b",
            "block-cursor-blurred-text-style": "i",
            "input-selection-background": "ansi_cyan",
            "input-cursor-text-style": "reverse",
            "scrollbar": "ansi_blue",
            "border-blurred": "ansi_bright_blue",
            "border": "ansi_cyan",
        },
    ),
    "frosted-ansi": TextualTheme(
        name="frosted-ansi",
        primary="ansi_bright_cyan",
        secondary="ansi_bright_white",
        warning="ansi_yellow",
        error="ansi_bright_red",
        success="ansi_bright_green",
        accent="ansi_bright_magenta",
        foreground="ansi_default",
        background="ansi_default",
        surface="ansi_default",
        panel="ansi_default",
        boost="ansi_default",
        dark=True,
        variables={
            "block-cursor-text-style": "b",
            "block-cursor-blurred-text-style": "i",
            "input-selection-background": "ansi_blue",
            "input-cursor-text-style": "reverse",
            "scrollbar": "ansi_bright_cyan",
            "border-blurred": "ansi_bright_white",
            "border": "ansi_blue",
        },
    ),
    "holographic-ansi": TextualTheme(
        name="holographic-ansi",
        primary="ansi_bright_magenta",
        secondary="ansi_bright_cyan",
        warning="ansi_yellow",
        error="ansi_red",
        success="ansi_green",
        accent="ansi_bright_blue",
        foreground="ansi_default",
        background="ansi_default",
        surface="ansi_default",
        panel="ansi_default",
        boost="ansi_default",
        dark=False,
        variables={
            "block-cursor-text-style": "b",
            "block-cursor-blurred-text-style": "i",
            "input-selection-background": "ansi_bright_magenta",
            "input-cursor-text-style": "reverse",
            "scrollbar": "ansi_blue",
            "border-blurred": "ansi_bright_cyan",
            "border": "ansi_bright_magenta",
        },
    ),
    "transparent_night-ansi": TextualTheme(
        name="transparent_night-ansi",
        primary="ansi_bright_blue",
        secondary="ansi_bright_white",
        warning="ansi_bright_yellow",
        error="ansi_bright_red",
        success="ansi_bright_green",
        accent="ansi_bright_cyan",
        foreground="ansi_default",
        background="ansi_default",
        surface="ansi_default",
        panel="ansi_default",
        boost="ansi_default",
        dark=True,
        variables={
            "block-cursor-text-style": "b",
            "block-cursor-blurred-text-style": "i",
            "input-selection-background": "ansi_blue",
            "input-cursor-text-style": "reverse",
            "scrollbar": "ansi_cyan",
            "border-blurred": "ansi_blue",
            "border": "ansi_bright_white",
        },
    ),
    # Warm Red Themes
    "warm_dark_red": TextualTheme(
        name="warm_dark_red",
        dark=True,
        background="#191919",
        foreground="#FF6B6B",  # Bright red
        primary="#FF4444",     # Primary red
        secondary="#CC0000",   # Deep red
        accent="#FF8080",      # Light red
        error="#D93025",
        success="#4CAF50",
        warning="#FFA726",
        surface="#222222",
        panel="#222222",
    ),
    "warm_light_red": TextualTheme(
        name="warm_light_red",
        dark=False,
        background="#FFF5F5",
        foreground="#CC0000",  # Deep red
        primary="#FF4444",     # Primary red
        secondary="#FF6B6B",   # Bright red
        accent="#FFCDD2",      # Soft red
        error="#D93025",
        success="#4CAF50",
        warning="#FFA726",
        surface="#FFF0F0",
        panel="#FFFFFF",
    ),

    # Warm Orange TextualThemes
    "warm_dark_orange": TextualTheme(
        name="warm_dark_orange",
        dark=True,
        background="#191919",
        foreground="#FFA07A",  # Light salmon
        primary="#FF7F50",     # Coral orange
        secondary="#FF4500",   # Deep orange
        accent="#FFB347",      # Light orange
        error="#D93025",
        success="#4CAF50",
        warning="#FFA726",
        surface="#222222",
        panel="#222222",
    ),
    "warm_light_orange": TextualTheme(
        name="warm_light_orange",
        dark=False,
        background="#FFF8F5",
        foreground="#FF4500",  # Deep orange
        primary="#FF7F50",     # Coral orange
        secondary="#FFA07A",   # Light salmon
        accent="#FFE4D6",      # Soft orange
        error="#D93025",
        success="#4CAF50",
        warning="#FFA726",
        surface="#FFF4ED",
        panel="#FFFFFF",
    ),

    # Warm Red-Yellow TextualThemes
    "warm_dark_red-yellow": TextualTheme(
        name="warm_dark_red-yellow",
        dark=True,
        background="#191919",
        foreground="#FFB347",  # Yellow-tinted red
        primary="#FF6B6B",     # Warm red
        secondary="#FFD700",   # Golden yellow
        accent="#FF8C42",      # Red-yellow blend
        error="#D93025",
        success="#4CAF50",
        warning="#FFA726",
        surface="#222222",
        panel="#222222",
    ),
    "warm_light_red-yellow": TextualTheme(
        name="warm_light_red-yellow",
        dark=False,
        background="#FFFAF5",
        foreground="#FF6B6B",  # Warm red
        primary="#FFB347",     # Yellow-tinted red
        secondary="#FFD700",   # Golden yellow
        accent="#FFE5CC",      # Soft red-yellow
        error="#D93025",
        success="#4CAF50",
        warning="#FFA726",
        surface="#FFF7F0",
        panel="#FFFFFF",
    ),

    # Warm Red-Orange TextualThemes
    "warm_dark_red-orange": TextualTheme(
        name="warm_dark_red-orange",
        dark=True,
        background="#191919",
        foreground="#FF7F50",  # Coral
        primary="#FF4444",     # Warm red
        secondary="#FF5722",   # Deep orange
        accent="#FF8C69",      # Red-orange blend
        error="#D93025",
        success="#4CAF50",
        warning="#FFA726",
        surface="#222222",
        panel="#222222",
    ),
    "warm_light_red-orange": TextualTheme(
        name="warm_light_red-orange",
        dark=False,
        background="#FFF6F5",
        foreground="#FF5722",  # Deep orange
        primary="#FF4444",     # Warm red
        secondary="#FF7F50",   # Coral
        accent="#FFE0D6",      # Soft red-orange
        error="#D93025",
        success="#4CAF50",
        warning="#FFA726",
        surface="#FFF2F0",
        panel="#FFFFFF",
    ),

    # Warm Yellow-Orange TextualThemes
    "warm_dark_yellow-orange": TextualTheme(
        name="warm_dark_yellow-orange",
        dark=True,
        background="#191919",
        foreground="#FFA726",  # Orange
        primary="#FFD700",     # Yellow
        secondary="#FF8C00",   # Dark orange
        accent="#FFB347",      # Yellow-orange blend
        error="#D93025",
        success="#4CAF50",
        warning="#FFA726",
        surface="#222222",
        panel="#222222",
    ),
    "warm_light_yellow-orange": TextualTheme(
        name="warm_light_yellow-orange",
        dark=False,
        background="#FFFBF5",
        foreground="#FF8C00",  # Dark orange
        primary="#FFD700",     # Yellow
        secondary="#FFA726",   # Orange
        accent="#FFE8CC",      # Soft yellow-orange
        error="#D93025",
        success="#4CAF50",
        warning="#FFA726",
        surface="#FFF7F0",
        panel="#FFFFFF",
    ),

    # Warm Yellow-Green TextualThemes
    "warm_dark_yellow-green": TextualTheme(
        name="warm_dark_yellow-green",
        dark=True,
        background="#191919",
        foreground="#9ACD32",  # Yellow-green
        primary="#FFD700",     # Yellow
        secondary="#6B8E23",   # Olive green
        accent="#C0D725",      # Light yellow-green
        error="#D93025",
        success="#4CAF50",
        warning="#FFA726",
        surface="#222222",
        panel="#222222",
    ),
    "warm_light_yellow-green": TextualTheme(
        name="warm_light_yellow-green",
        dark=False,
        background="#FAFFF5",
        foreground="#6B8E23",  # Olive green
        primary="#FFD700",     # Yellow
        secondary="#9ACD32",   # Yellow-green
        accent="#E6F0CC",      # Soft yellow-green
        error="#D93025",
        success="#4CAF50",
        warning="#FFA726",
        surface="#F5FAF0",
        panel="#FFFFFF",
    ),

    # Warm Green-Orange TextualThemes
    "warm_dark_green-orange": TextualTheme(
        name="warm_dark_green-orange",
        dark=True,
        background="#191919",
        foreground="#FFA726",  # Orange
        primary="#6B8E23",     # Olive green
        secondary="#FF8C00",   # Dark orange
        accent="#A4C639",      # Green-orange blend
        error="#D93025",
        success="#4CAF50",
        warning="#FFA726",
        surface="#222222",
        panel="#222222",
    ),
    "warm_light_green-orange": TextualTheme(
        name="warm_light_green-orange",
        dark=False,
        background="#FFF9F5",
        foreground="#6B8E23",  # Olive green
        primary="#FFA726",     # Orange
        secondary="#8FB339",   # Light olive
        accent="#FFE6CC",      # Soft orange
        error="#D93025",
        success="#4CAF50",
        warning="#FFA726",
        surface="#FFF5F0",
        panel="#FFFFFF",
    ),

    # Warm Red-Green TextualThemes
    "warm_dark_red-green": TextualTheme(
        name="warm_dark_red-green",
        dark=True,
        background="#191919",
        foreground="#FF6B6B",  # Warm red
        primary="#6B8E23",     # Olive green
        secondary="#CC0000",   # Deep red
        accent="#A4C639",      # Green blend
        error="#D93025",
        success="#4CAF50",
        warning="#FFA726",
        surface="#222222",
        panel="#222222",
    ),
    "warm_light_red-green": TextualTheme(
        name="warm_light_red-green",
        dark=False,
        background="#FFF8F5",
        foreground="#CC0000",  # Deep red
        primary="#6B8E23",     # Olive green
        secondary="#FF6B6B",   # Warm red
        accent="#E6F0CC",      # Soft green
        error="#D93025",
        success="#4CAF50",
        warning="#FFA726",
        surface="#FFF4F0",
        panel="#FFFFFF",
    ),
}