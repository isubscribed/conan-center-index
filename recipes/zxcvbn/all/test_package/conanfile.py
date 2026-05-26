from conan import ConanFile
from conan.tools.build import can_run
from conan.tools.cmake import cmake_layout, CMake, CMakeToolchain
import os

class ZxcvbnTestPackageConan(ConanFile):
    settings = "os", "arch", "compiler", "build_type"
    generators = "CMakeDeps", "VirtualRunEnv"
    test_type = "explicit"

    def layout(self):
        cmake_layout(self)

    def requirements(self):
        self.requires(self.tested_reference_str)

    def generate(self):
        tc = CMakeToolchain(self)
        dep = self.dependencies[self.tested_reference_str]
        if dep.options.get_safe("use_dict_file"):
            dict_path = os.path.join(dep.package_folder, dep.cpp_info.bindirs[0], "zxcvbn.dict").replace("\\", "/")
            tc.preprocessor_definitions["ZXCVBN_DICT_FILE"] = f'"{dict_path}"'
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        if can_run(self):
            bin_path = os.path.join(self.cpp.build.bindir, "test_package")
            self.run(bin_path, env="conanrun")
