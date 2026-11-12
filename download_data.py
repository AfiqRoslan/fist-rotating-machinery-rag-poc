"""Download the three official FIST PDFs. Requires an internet connection."""
import json
from pathlib import Path
import requests

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "data" / "pdfs"


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    sources = json.loads((ROOT / "sources.json").read_text(encoding="utf-8"))
    for src in sources:
        destination = OUT / src["filename"]
        if destination.exists() and destination.read_bytes()[:4] == b"%PDF":
            print(f"[OK] Present: {destination.name}")
            continue
        print(f"[GET] {src['title']}")
        try:
            with requests.get(src["url"], timeout=75, stream=True,
                              headers={"User-Agent": "FYP-Academic-Research/1.0"}) as response:
                response.raise_for_status()
                temp = destination.with_suffix(".partial")
                with temp.open("wb") as f:
                    for block in response.iter_content(1024 * 128):
                        if block:
                            f.write(block)
                if temp.stat().st_size < 10000 or temp.read_bytes()[:4] != b"%PDF":
                    temp.unlink(missing_ok=True)
                    raise ValueError("Response is not a valid PDF")
                temp.replace(destination)
            print(f"[SAVED] {destination.name}: {destination.stat().st_size/1048576:.1f} MB")
        except (requests.RequestException, OSError, ValueError) as err:
            print(f"[FAILED] {err}")
            print("  Download the official PDF manually using the link in sources.json")
            print(f"  Then save it to: {destination}")
    found = sum((OUT/s['filename']).exists() for s in sources)
    print(f"\nPDFs present: {found}/{len(sources)}")
    if not found:
        raise SystemExit("No PDFs downloaded; see manual instructions in README.md")


if __name__ == "__main__":
    main()
