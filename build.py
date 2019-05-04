from cpt.packager import ConanMultiPackager

if __name__ == "__main__":
    remotes = [("https://api.bintray.com/conan/bincrafters/public-conan", True, "bincrafters")]

    builder = ConanMultiPackager(remotes=remotes, build_policy="missing", build_types=["Release"])
    builder.add_common_builds(shared_option_name="kf5-attica:shared")
    builder.run()
