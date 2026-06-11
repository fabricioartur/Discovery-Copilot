"""Generate PNG example visuals for the Northstar scenario.

This script is intentionally optional. The generated PNG files are committed so
the repository can be viewed without installing Pillow.
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
VISUALS = ROOT / "examples" / "northstar_retail_group" / "visuals"

BG = "#f8fafc"
INK = "#0f172a"
TEXT = "#475467"
BORDER = "#cbd5e1"
BLUE = "#2f80ed"
BLUE_LIGHT = "#eef6ff"
GREEN = "#16a34a"
GREEN_LIGHT = "#f0fdf4"
ORANGE = "#f97316"
ORANGE_LIGHT = "#fff7ed"
GRAY_LIGHT = "#f8fafc"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    font_paths = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/Supplemental/Helvetica Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Helvetica.ttf",
        "/Library/Fonts/Arial Bold.ttf" if bold else "/Library/Fonts/Arial.ttf",
    ]
    for path in font_paths:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


TITLE = font(42, True)
SUBTITLE = font(22)
H2 = font(26, True)
BODY = font(18)
BODY_BOLD = font(18, True)
SMALL = font(15)
METRIC = font(54, True)


def canvas(width: int = 1400, height: int = 788) -> tuple[Image.Image, ImageDraw.ImageDraw]:
    image = Image.new("RGB", (width, height), BG)
    return image, ImageDraw.Draw(image)


def rounded(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], fill: str, outline: str = BORDER, radius: int = 18) -> None:
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=2)


def centered(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], text: str, fill: str = INK, fnt: ImageFont.ImageFont = BODY_BOLD) -> None:
    bbox = draw.textbbox((0, 0), text, font=fnt)
    x = box[0] + (box[2] - box[0] - (bbox[2] - bbox[0])) / 2
    y = box[1] + (box[3] - box[1] - (bbox[3] - bbox[1])) / 2 - 2
    draw.text((x, y), text, fill=fill, font=fnt)


def arrow(draw: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int], color: str = "#344054") -> None:
    draw.line([start, end], fill=color, width=3)
    x, y = end
    draw.polygon([(x, y), (x - 12, y - 7), (x - 12, y + 7)], fill=color)


def save(image: Image.Image, name: str) -> None:
    VISUALS.mkdir(parents=True, exist_ok=True)
    image.save(VISUALS / name, "PNG", optimize=True)


def draw_header(draw: ImageDraw.ImageDraw, title: str, subtitle: str) -> None:
    draw.text((70, 52), title, fill=INK, font=TITLE)
    draw.text((70, 105), subtitle, fill=TEXT, font=SUBTITLE)


def build_banner() -> None:
    image, draw = canvas(1400, 630)
    draw_header(
        draw,
        "Discovery Copilot",
        "Python CLI for enterprise discovery analysis and pre-sales documentation",
    )

    cards = [
        (70, 185, 370, 405, "Input", ".txt / .md discovery notes", BLUE_LIGHT, BLUE),
        (410, 185, 710, 405, "AI Analysis", "OpenAI or local mock provider", GREEN_LIGHT, GREEN),
        (750, 185, 1050, 405, "Outputs", "11 structured Markdown reports", ORANGE_LIGHT, ORANGE),
        (1090, 185, 1330, 405, "Case", "Northstar enterprise example", GRAY_LIGHT, "#64748b"),
    ]
    for box in cards:
        x1, y1, x2, y2, title, subtitle, fill, outline = box
        rounded(draw, (x1, y1, x2, y2), fill, outline)
        draw.text((x1 + 28, y1 + 40), title, fill=INK, font=H2)
        draw.text((x1 + 28, y1 + 88), subtitle, fill=TEXT, font=BODY)

    for x in (382, 722, 1062):
        arrow(draw, (x, 295), (x + 18, 295))

    rounded(draw, (70, 470, 1330, 560), "#ffffff")
    draw.text((105, 500), "Project signal:", fill=INK, font=BODY_BOLD)
    draw.text(
        (260, 500),
        "shows product thinking, discovery quality, solution framing, and runnable code.",
        fill=TEXT,
        font=BODY,
    )
    save(image, "overview_banner.png")


def build_workflow() -> None:
    image, draw = canvas()
    draw_header(
        draw,
        "Discovery Copilot Workflow",
        "Actual project flow: local notes, Python CLI, provider, and Markdown outputs",
    )

    steps = [
        (70, 210, 280, 330, "Discovery Notes", "Customer context\nmeeting notes"),
        (355, 210, 565, 330, "Python CLI", "main.py\ninput validation"),
        (640, 210, 850, 330, "Prompts", "report templates\n11 definitions"),
        (925, 210, 1135, 330, "Provider", "OpenAI API\nor mock mode"),
        (1210, 210, 1350, 330, "Reports", "output/*.md"),
    ]

    for x1, y1, x2, y2, title, detail in steps:
        rounded(draw, (x1, y1, x2, y2), "#ffffff")
        centered(draw, (x1, y1 + 18, x2, y1 + 55), title, fnt=BODY_BOLD)
        lines = detail.splitlines()
        for i, line in enumerate(lines):
            centered(draw, (x1, y1 + 60 + i * 25, x2, y1 + 90 + i * 25), line, fill=TEXT, fnt=SMALL)

    for start_x in (280, 565, 850, 1135):
        arrow(draw, (start_x + 18, 270), (start_x + 58, 270))

    rounded(draw, (130, 455, 610, 650), BLUE_LIGHT, BLUE)
    draw.text((165, 490), "Mock mode", fill=INK, font=H2)
    draw.text((165, 535), "Runs locally without an API key.", fill=TEXT, font=BODY)
    draw.text((165, 565), "Useful for reviewing the project without external services.", fill=TEXT, font=BODY)

    rounded(draw, (790, 455, 1270, 650), GREEN_LIGHT, GREEN)
    draw.text((825, 490), "OpenAI mode", fill=INK, font=H2)
    draw.text((825, 535), "Uses the configured model for full analysis.", fill=TEXT, font=BODY)
    draw.text((825, 565), "Same CLI, same report structure.", fill=TEXT, font=BODY)
    save(image, "discovery_copilot_workflow.png")


def build_architecture() -> None:
    image, draw = canvas()
    draw_header(
        draw,
        "Northstar Target Architecture",
        "Recommended customer solution from the fictional discovery scenario",
    )

    columns = [
        (70, 190, 270, 610, "Users", ["Agents", "Store managers", "Support ops"], BLUE_LIGHT, BLUE),
        (330, 190, 530, 610, "Access", ["Entra ID", "RBAC", "Audit policy"], GREEN_LIGHT, GREEN),
        (590, 190, 840, 610, "AI layer", ["Assistant UX", "Orchestrator", "PII redaction", "RAG"], ORANGE_LIGHT, ORANGE),
        (900, 190, 1100, 610, "Integration", ["MuleSoft APIs", "SOAP adapters", "Batch bridges"], BLUE_LIGHT, BLUE),
        (1160, 190, 1330, 650, "Systems", ["Salesforce", "Zendesk", "OMS", "SAP", "Oracle", "Snowflake"], GRAY_LIGHT, "#64748b"),
    ]
    center_y = 400
    prev_right = None
    for x1, y1, x2, y2, title, items, fill, outline in columns:
        rounded(draw, (x1, y1, x2, y2), "#ffffff")
        draw.text((x1 + 24, y1 + 26), title, fill=INK, font=H2)
        y = y1 + 82
        for item in items:
            rounded(draw, (x1 + 24, y, x2 - 24, y + 48), fill, outline, radius=12)
            centered(draw, (x1 + 24, y, x2 - 24, y + 48), item, fnt=SMALL)
            y += 58
        if prev_right is not None:
            arrow(draw, (prev_right + 18, center_y), (x1 - 18, center_y))
        prev_right = x2

    draw.text(
        (130, 705),
        "Phase one stays human-in-the-loop: read-heavy ERP access, approved knowledge, redaction, RBAC, and audit logging.",
        fill=TEXT,
        font=BODY,
    )
    save(image, "northstar_target_architecture.png")


def build_scores() -> None:
    image, draw = canvas()
    draw_header(
        draw,
        "Discovery Quality and Requirements Coverage",
        "Sample metrics produced for the Northstar Retail Group enterprise scenario",
    )

    scores = [
        ("Business", 82),
        ("Technical", 76),
        ("Security", 68),
        ("Stakeholders", 84),
        ("Requirements", 71),
        ("Risk", 79),
        ("Architecture", 74),
        ("Overall", 76),
    ]
    x = 95
    for label, score in scores:
        bar_h = int(score * 2.8)
        draw.rounded_rectangle((x, 455 - bar_h, x + 92, 455), radius=12, fill=BLUE)
        centered(draw, (x, 470, x + 92, 510), label, fill=TEXT, fnt=SMALL)
        centered(draw, (x, 455 - bar_h - 45, x + 92, 455 - bar_h - 10), str(score), fill=INK, fnt=BODY_BOLD)
        x += 155

    rounded(draw, (70, 570, 1330, 705), "#ffffff")
    coverage = [
        ("Business", "80%"),
        ("Technical", "69%"),
        ("Security", "58%"),
        ("Integration", "73%"),
        ("Infra", "56%"),
        ("Metrics", "50%"),
        ("Stakeholders", "88%"),
    ]
    x = 110
    for label, value in coverage:
        draw.text((x, 602), value, fill=INK, font=H2)
        draw.text((x, 640), label, fill=TEXT, font=SMALL)
        x += 175

    save(image, "discovery_scores_and_coverage.png")


def main() -> None:
    build_banner()
    build_workflow()
    build_architecture()
    build_scores()


if __name__ == "__main__":
    main()
