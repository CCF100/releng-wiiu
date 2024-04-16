subarch: rv32_ilp32_musl
target: stage1
version_stamp: @TIMESTAMP@
interpreter: /usr/bin/qemu-riscv32
rel_type: 23.0-musl
profile: default/linux/riscv/23.0/rv32/ilp32/musl
snapshot_treeish: @TREEISH@
source_subpath: 23.0-musl/stage3-rv32_ilp32_musl-latest
compression_mode: pixz
decompressor_search_order: xz bzip2
update_seed: yes
update_seed_command: -uDN @world
portage_confdir: @REPO_DIR@/releases/portage/stages-qemu
portage_prefix: releng
