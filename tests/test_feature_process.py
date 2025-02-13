import pytest
from blueOceanField.domain.feature import Remove, FeatureProcessMeta

@pytest.fixture
def input_data():
    """ テスト用の入力データ """
    return {"a": 1.0, "b": 2.0, "c": 3.0, "x": 4.0, "y": 5.0, "z": 6.0}

def test_metadata_registration():
    """ メタクラスが正しくメタデータを登録しているか確認 """
    metadata = FeatureProcessMeta.registry.get("Remove")

    assert metadata is not None, "Remove のメタデータが登録されていない"
    assert "parameters" in metadata, "パラメータ情報が正しく登録されていない"
    assert "targets" in metadata["parameters"], "targets パラメータが登録されていない"
    assert metadata["parameters"]["targets"]["value"] == [], "targets のデフォルト値が間違っている"
    assert metadata["parameters"]["targets"]["type"] == "list", "targets の型情報が間違っている"

def test_instance_variable_assignment():
    """ `Remove` インスタンスごとに異なる `targets` が適用されるか確認 """
    remove1 = Remove(targets=["a", "b"])
    remove2 = Remove(targets=["x", "y", "z"])

    assert remove1.targets == ["a", "b"], "remove1 の targets が正しく設定されていない"
    assert remove2.targets == ["x", "y", "z"], "remove2 の targets が正しく設定されていない"
    assert remove1.targets != remove2.targets, "異なるインスタンスの targets が共有されてしまっている"

def test_execute_removes_specified_keys(input_data):
    """ `execute` メソッドが `targets` に応じて正しく動作するか確認 """
    remove1 = Remove(targets=["a", "b"])
    remove2 = Remove(targets=["x", "y", "z"])

    result1 = remove1.execute(input_data)
    result2 = remove2.execute(input_data)

    assert result1 == {"c": 3.0, "x": 4.0, "y": 5.0, "z": 6.0}, "remove1 の削除処理が正しくない"
    assert result2 == {"a": 1.0, "b": 2.0, "c": 3.0}, "remove2 の削除処理が正しくない"

def test_default_parameter():
    """ パラメータを指定しない場合、デフォルト値が適用されるか確認 """
    remove = Remove()

    assert remove.targets == [], "デフォルト値が正しく適用されていない"

def test_metadata_json():
    """ メタデータの JSON 変換が正しく行われるか確認 """
    import json
    metadata_json = json.dumps(FeatureProcessMeta.registry, indent=4, ensure_ascii=False)

    assert "Remove" in metadata_json, "メタデータ JSON に Remove クラスが含まれていない"
    assert '"targets"' in metadata_json, "メタデータ JSON に targets が含まれていない"
