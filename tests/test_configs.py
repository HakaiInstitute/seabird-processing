import subprocess
import pytest
from seabird_processing.configs import AlignCTDConfig, DatCnvConfig
from tests.utils import make_empty


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


def test_error_catch(tmp_path):
    output_dir = tmp_path
    xmlcon_path = "./tests/files/xmlcon/19-7674-20200126.xmlcon"
    psa_datcnv_path = make_empty(tmp_path / "psa_datcnv.psa")

    converter = DatCnvConfig(
        output_dir=output_dir,
        xmlcon=xmlcon_path,
        psa=psa_datcnv_path,
        output_file_suffix="_datcnv",
    )

    # Assert error is raised
    with pytest.raises(subprocess.CalledProcessError):
        converter.run("./tests/files/SBE19plus_01907674_2020_02_05_0001.hex")
