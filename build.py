from cpt.packager import ConanMultiPackager

if __name__ == "__main__":
    remotes = [
        ("https://api.bintray.com/conan/appimage-conan-community/public-conan", True, "appimage-conan-community"),
        ("https://api.bintray.com/conan/azubieta/AppImage", True, "azubieta")
    ]

    builder = ConanMultiPackager(remotes=remotes, build_policy="missing", build_types=["Release"])
    builder.add_common_builds(shared_option_name="kf5-attica:shared")
    builder.run()
