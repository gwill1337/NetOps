from jinja2 import Environment, FileSystemLoader

# Автовыбор шаблона по OS
TEMPLATE_MAP = {
    "cisco": "cisco.j2",
    "cisco-ios": "cisco.j2",
    "ios": "cisco.j2",
    "ios-xe": "cisco.j2",

    "juniper": "juniper.j2",
    "junos": "juniper.j2",

    "paloalto": "paloalto.j2",
    "panos": "paloalto.j2",
    "pan-os": "paloalto.j2"
}

def render_config(data):
    os_type = data["os"].lower()

    if os_type not in TEMPLATE_MAP:
        raise ValueError(f"OS '{data['os']}' не поддерживается")

    env = Environment(
        loader=FileSystemLoader("templates"),
        trim_blocks=True,
        lstrip_blocks=True
    )

    template = env.get_template(TEMPLATE_MAP[os_type])
    return template.render(**data)

    rendered = render_config(device)
    print(rendered)
