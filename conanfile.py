from conans import ConanFile, CMake, tools


class Kf5atticaConan(ConanFile):
    name = "kf5-attica"
    version = "5.57.0"
    license = "MIT"
    author = "Alexis Lopez Zubieta contact@azubieta.net"
    url = "https://github.com/appimage-conan-community/conan-kf5-attica"
    description = "Attica is a Qt library that implements the Open Collaboration Services API"
    topics = ("kf5", "qt", "ocs")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake_paths"
    # build_requires = "cmake_installer/3.13.0@conan/stable"
    requires = ("extra-cmake-modules/5.57.0@appimage-conan-community/stable", "qt/5.12.3@appimage-conan-community/stable")

    def system_requirements(self):
        pkgs_name = None
        if tools.os_info.linux_distro == "ubuntu":
            pkgs_name = ["libicu-dev", "libglib2.0-dev"]

        if pkgs_name:
            installer = tools.SystemPackageTool()
            for pkg_name in pkgs_name:
                installer.install(pkg_name)

    def source(self):
        self.run("git clone https://github.com/KDE/attica.git --depth=1 --branch=v5.57.0")

    def build(self):
        cmake = CMake(self)
        cmake.definitions["ATTICA_STATIC_BUILD"] = not self.options.shared
        cmake.definitions["CMAKE_PROJECT_Attica_INCLUDE"] = self.build_folder + "/conan_paths.cmake"
        cmake.configure(source_folder="attica")
        cmake.build()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["KF5Attica"]
        self.cpp_info.builddirs = ["lib/cmake/KF5Attica/"]
        self.cpp_info.includedirs = "include/KF5"
