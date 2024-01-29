
import argparse
import os
import yaml

def translate_yaml_to_md(input_folder, output_folder):
    for root, dirs, files in os.walk(input_folder):
        if "description.yaml" in files:
            with open(os.path.join(root, "description.yaml"), "r") as f:
                print(f)
                description = yaml.safe_load(f)
                name = description.get("rom", None)
                if name is None:
                    continue
                enablestatefile = description.get("enablestatefile", None)
                author = description.get("author", None)
                version = description.get("version", None)
                game = description.get("game", None)
                year = description.get("year", None)
                style = description.get("style", None)
                orientation = description.get("crt", {}).get("orientation", None)
                parts = description.get("parts", [])
                num_parts = len(parts)
                md5sum = description.get("md5sum", None)
                has_video_file = "No"
                if "video" in description and "file" in description["video"]:
                    has_video_file = "Yes"
                has_model_file = "No"
                if "model" in description and "file" in description["model"]:
                    has_model_file = "Yes"
                tags = ["rom", "compatData"]
                data = {
                    "rom": name,
                    "author": author,
                    "version": version,
                    "game": game or name,
                    "enablestatefile": enablestatefile,
                    "year": year,
                    "style": style,
                    "real cabinet": "yes",
                    "crt": {"orientation": orientation},
                    "parts": num_parts,
                    "tags": tags,
                    "md5sum": md5sum,
                    "video": has_video_file,
                    "model": has_model_file
                }
                output_file = os.path.join(output_folder, f"{name}.md")
                with open(output_file, "w") as f:
                    f.write("---\n")
                    f.write(yaml.dump(data))
                    f.write("---\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Translate YAML files to Markdown")
    parser.add_argument("input_folder", type=str, help="Input folder containing YAML files")
    parser.add_argument("output_folder", type=str, help="Output folder for translated Markdown files")
    args = parser.parse_args()
    
    translate_yaml_to_md(args.input_folder, args.output_folder)
