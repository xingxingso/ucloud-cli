# UTiDB CLI 线上测试

## 只读查询测试 (Read-Only)

* Execute command: "ucloud -p prod utidb list --output json"
* Execute command: "ucloud -p prod utidb list --output json --limit 10 --offset 0"

## 帮助信息验证

* Execute command: "ucloud -p prod utidb --help"
* Execute command: "ucloud -p prod utidb list --help"
* Execute command: "ucloud -p prod utidb describe --help"
* Execute command: "ucloud -p prod utidb create --help"
* Execute command: "ucloud -p prod utidb delete --help"
* Execute command: "ucloud -p prod utidb backup --help"
* Execute command: "ucloud -p prod utidb list-backup --help"
* Execute command: "ucloud -p prod utidb scale-node --help"
* Execute command: "ucloud -p prod utidb resize-disk --help"
* Execute command: "ucloud -p prod utidb modify-spec --help"
* Execute command: "ucloud -p prod utidb list-specs --help"
