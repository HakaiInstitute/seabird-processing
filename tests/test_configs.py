from pathlib import Path

from seabird_processing.configs import AlignCTDConfig


def make_empty(path: Path) -> Path:
    """Create an empty file at the given path."""
    assert not path.is_file(), "File already exists"
    with open(path, "w") as f:
        f.write("")
    return path


def test_align_ctd_batch_string(tmp_path):
    output_dir = tmp_path
    xmlcon_path = make_empty(tmp_path / "xmlcon.xml")
    psa_path = make_empty(tmp_path / "psa.psa")

    config = AlignCTDConfig(
        output_dir=output_dir,
        xmlcon=xmlcon_path,
        psa=psa_path,
        output_file_suffix="_aligned",
    )

    exec_str = config.get_exec_str("*.cnv", batch_mode=True)
    assert type(exec_str) == str

    assert exec_str == (
        f"alignctd "
        f"/c{xmlcon_path} "
        f"/i*.cnv "
        f"/o{output_dir}\\ "
        f"/p{psa_path} "
        f"/a_aligned "
        f"/s"
    )
