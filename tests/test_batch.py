from seabird_processing import configs, Batch
from tests.utils import make_empty


def test_simple_batch_string(tmp_path):
    output_dir = tmp_path
    xmlcon_path = make_empty(tmp_path / "xmlcon.xml")
    psa_align_path = make_empty(tmp_path / "psa_align.psa")
    psa_datcnv_path = make_empty(tmp_path / "psa_datcnv.psa")

    batch = Batch(
        [
            configs.DatCnvConfig(
                output_dir=output_dir,
                xmlcon=xmlcon_path,
                psa=psa_datcnv_path,
                output_file_suffix="_datcnv",
            ),
            configs.AlignCTDConfig(
                output_dir=output_dir,
                xmlcon=xmlcon_path,
                psa=psa_align_path,
                output_file_suffix="_aligned",
            ),
        ]
    )

    exec_str = batch.get_batch_config_str("*.hex")
    assert type(exec_str) == str

    assert exec_str.split("\n") == [
        f"{batch.config_header_comment}",
        f"datcnv /c{xmlcon_path} /i*.hex /o{output_dir}\\ /p{psa_datcnv_path} "
        f"/a_datcnv /s",
        f"alignctd /c{xmlcon_path} /i*_datcnv.cnv /o{output_dir}\\ /p{psa_align_path} "
        f"/a_aligned /s",
    ]
