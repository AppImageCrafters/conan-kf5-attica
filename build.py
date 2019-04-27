from cpt.packager import ConanMultiPackager

if __name__ == "__main__":
    remotes = [
        ("https://api.bintray.com/conan/appimage-conan-community/public-conan", True, "appimage-conan-community"),
        ("https://api.bintray.com/conan/azubieta/AppImage", True, "azubieta")
    ]

    command = "sudo apt-get -qq update && sudo apt-get -qq install -y libicu-dev"

    builder = ConanMultiPackager(remotes=remotes, build_policy="missing", docker_entry_script=command,
                                 build_types=["Release"])
    builder.add_common_builds(shared_option_name="kf5-attica:shared")
    builder.run()
