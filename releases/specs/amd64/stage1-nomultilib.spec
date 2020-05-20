subarch: amd64
target: stage1
version_stamp: nomultilib-@TIMESTAMP@
rel_type: default
profile: default/linux/amd64/17.1/no-multilib
snapshot: @TIMESTAMP@
source_subpath: default/stage3-amd64-nomultilib-latest
compression_mode: pixz_x
update_seed: yes
update_seed_command: --update --deep --newuse @world
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
