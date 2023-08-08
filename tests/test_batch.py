from pathlib import Path

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
        (
            f"datcnv "
            f"/c{xmlcon_path} "
            f"/i*.hex "
            f"/o{output_dir}\\ "
            f"/p{psa_datcnv_path} "
            f"/a_datcnv "
            f"/s"
        ),
        (
            f"alignctd "
            f"/c{xmlcon_path} "
            f"/i{output_dir}\\*_datcnv.cnv "
            f"/o{output_dir}\\ "
            f"/p{psa_align_path} "
            f"/a_aligned "
            f"/s"
        ),
    ]


def test_batch(tmp_path):
    output_dir = tmp_path
    for d in range(1, 9):
        (output_dir / str(d)).mkdir(exist_ok=True)
    xmlcon_path = "./tests/files/xmlcon/19-7674-20200126.xmlcon"
    batch = Batch(
        [
            configs.DatCnvConfig(
                output_dir=f"{output_dir}/1",
                xmlcon=xmlcon_path,
                psa="./tests/files/psa/DatCnv-7674-20181210.psa",
                # output_file_suffix="_datcnv",
            ),
            configs.FilterConfig(
                output_dir=f"{output_dir}/2",
                xmlcon=xmlcon_path,
                psa="./tests/files/psa/Filter.psa",
                # output_file_suffix="_filter",
            ),
            configs.AlignCTDConfig(
                output_dir=f"{output_dir}/3",
                xmlcon=xmlcon_path,
                psa="./tests/files/psa/AlignCTD-7674-20181210.psa",
                # output_file_suffix="_alignctd",
            ),
            configs.CellTMConfig(
                output_dir=f"{output_dir}/4",
                xmlcon=xmlcon_path,
                psa="./tests/files/psa/CellTM-7674-20140307.psa",
                # output_file_suffix="_celltm",
            ),
            configs.LoopEditConfig(
                output_dir=f"{output_dir}/5",
                xmlcon=xmlcon_path,
                psa="./tests/files/psa/LoopEdit-7674-20140307.psa",
                # output_file_suffix="_loopedit",
            ),
            configs.DeriveConfig(
                output_dir=f"{output_dir}/6",
                xmlcon=xmlcon_path,
                psa="./tests/files/psa/Derive-7674-20140307.psa",
                # output_file_suffix="_derive",
            ),
            configs.DeriveTEOS10Config(
                output_dir=f"{output_dir}/7",
                xmlcon=xmlcon_path,
                psa="./tests/files/psa/DeriveTEOS10-7674-20140307.psa",
                # output_file_suffix="_deriveteos10",
            ),
            configs.BinAvgConfig(
                output_dir=f"{output_dir}/8",
                xmlcon=xmlcon_path,
                psa="./tests/files/psa/BinAvg-7674-20140307.psa",
                # output_file_suffix="_binavg",
            ),
        ]
    )

    batch.run("./tests/files/*.hex")
    for i in range(1, 9):
        assert Path(
            f"{output_dir}/{i}/SBE19plus_01907674_2020_02_05_0001.cnv"
        ).is_file()
