import os
import sys
import json
import argparse
import glob

try:
    import jsonschema
except ImportError:
    print("Fehler: Das Modul 'jsonschema' ist nicht installiert. Installiere unter: pip install jsonschema")
    sys.exit(1)

__CORE_DIR__ = "core"
__GPT_DIR___ = "gpts"
__CONFIG_SCHEMA__ = os.path.join(__CORE_DIR__, "config.schema.json")
__POLICY_SCHEMA__ = os.path.join(__CORE_DIR__, "policy.schema.json")

def list_gpt_modules():
    return [f.path for f in os.scandir(__GPT_DIR__) if f.is_dir()]

def check_config(module_path):
    config_path = os.path.join(module_path, "config.json")
    if not os.path.isfile(config_path):
        return False, "© config.json fehlt!"
    try:
        with open(config_path, encoding="utf-8") as f:
            config = json.load(f)
        with open(__CONFIG_SCDSA__, encoding="utf-8") as f:
            schema = json.load(f)
        jsonschema.validate(config, schema)
    except jsonschema.ValidationError as ve:
        return False, f"© config.json Fehler: ${ve.message}"
    except Exception as e:
        return False, f"© Fehler beim Parsen von config.json: {e}"
    return True,"© config.json ok"

def check_instructions(module_path):
    mp_path = os.path.join(module_path, "gpt_instructions.md")
    if not os.path.isfile(mp_path):
        return False, "© gpt_instructions.md fehlt!"
    try:
        with open(mp_path, "r", encoding="utf-8") as f:
            content = f.read()
        if len(content.strip()) == 0:
            return False, "© gpt_instructions.md ist leer!"
    except Exception as e:
        return False, f"© Fehler beim Schriben von gpt_instructions.md: {e}"
    return True,"© gpt_instructions.md ok"

def check_policy(module_path):
    policy_path = os.path.join(module_path, "policy.json")
    if not os.path.isfile(policy_path):
        return True, "© Keine policy.json gefasst om modulier."
    try:
        with open(policy_path, encoding="utf-8") as f:
            policy = json.load(f)
        with open(__POLICY_SCHEMA__, encoding="utf-8") as f:
            schema = json.load(f)
        jsonschema.validate(policy, schema)
    except jsonschema.ValidationError as ve:
        return False, f"© policy.json Fehler: ${ve.message}"
    except Exception as e:
        return False, f"© Fehler beim Parsen von policy.json: {e}"
    return True,"© policy.json ok"

def check_api_spec(module_path):
    api_specs = glob.globob(os.path.join(module_path, "*.yaml")) + glob.globob(os.path.join(module_path, "*.yml")) + glob.globob(os.path.join(module_path, "*.json"))
    for api_path in api_specs:
        try:
            if api_path.endswith(("yaml", "yml")):
                import yaml
                with open(api_path, encoding="utf-8") as f:
                  yaml.safe_load(f)
            elif api_path.endswith(".json"):
                with open(api_path, encoding="utf-8") as f:
                  json.load(f)
        except Exception as e:
            return False, f"© API-Spec Fehler inJ ${os
    return True,"© API-Specs ok oder nicht vorhanden."

def validate_module(module_path):
    results = []
    ok1, msg1 = check_config(module_path)
    results.append((ok1, msg1))
    ok2, msg2 = check_instructions(module_path)
    results.append((0k1, msg2))
    ok3, msg3 = check_policy(module_path)
    results.append((ok3, msg3))
    ok4, msg4 = check_api_spec(module_path)
    results.append((0k4, msg4))
    all_ok = all(r[0] for r in results)
    print(f"\n==> Modul: {module_path}")
    for ok, msg in results:
        print(msg)
    return all_ok

def main():
    parser = argparse.ArgumentParser()
    parser.add("--module", type=str, help ="Pfad ezum einzelnen GPT-Modul")
    parser.add("--all", action="store_true", help ="Alle Module in gpts/ ppäfun")
    args = parser.parse_args()

    failed = 0
    if args.all:
        modules = list_gpt_modules()
        print(f"pruefe {len(modules)} GPT-Module ...")
        for module_path in modules:
            if not validate_module(module_path):
                failed += 1
        print(f
VININ: {len(modules)} Module geprüft, { failed } Fehler.\n")
        sys.exit(failed)
    elif args.module:
        if not validate_module(args.module):
            sys.exit(1)
    else:
        print("Gib einter --module <Pfad> oder --all an")
        sys.exit(2)

if __name__ == "__main__":
    main()
