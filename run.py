import argparse
from lib.process3d import process3d

# SOME TIPS FOR INSTALLATION ON MAC: WRITTEN BY JOHN SEONG
# -------------------------------------------
# brew install libomp on macOS
# export LDFLAGS="-L/opt/homebrew/opt/libomp/lib"
# export CPPFLAGS="-I/opt/homebrew/opt/libomp/include"
# -------------------------------------------
# Run git clone --recurse-submodules https://github.com/pybind/pybind11.git for pybind11 folder
#
# Ceres Version Requirements: 2.1.0_2
# # CMake
# brew install cmake
# # google-glog and gflags
# brew install glog gflags
# # Eigen3
# brew install eigen
# # SuiteSparse
# brew install suite-sparse
    # curl http://ceres-solver.org/ceres-solver-2.1.0.tar.gz > ceres-solver-2.1.0.tar.gz
#     tar zxf ceres-solver-2.1.0.tar.gz
# mkdir ceres-bin
# cd ceres-bin
# cmake ../ceres-solver-2.1.0
# make -j3
# make test
# # Optionally install Ceres, it can also be exported using CMake which
# # allows Ceres to be used without requiring installation, see the
# # documentation for the EXPORT_BUILD_DIR option for more information.
# make install
# VVIP: When you're running a script, use the following command to set the Python version to 3.9, python3.9 run.py
# cd cpp
# mkdir build
# cd build
# cmake ..
# make
# make install (do not run as sudo!)

if __name__ == "__main__":
    class ArgumentParserWithDefaults(argparse.ArgumentParser):
        def add_argument(self, *args, help=None, default=None, **kwargs):
            if help is not None:
                kwargs["help"] = help
            if default is not None and args[0] != "-h":
                kwargs["default"] = default
                if help is not None:
                    kwargs["help"] += " (default: {})".format(default)
            super().add_argument(*args, **kwargs)

    parser = ArgumentParserWithDefaults(description="TrueDepth camera point cloud registration",
        formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument("folder", help="folder containing bins and camera calibration")
    parser.add_argument("--viz", type=int, default=1, help="visualize result")

    method = "Registration method\n"
    method += "0: sequential ICP\n"
    method += "1: sequential ICP with loop closure\n"
    method += "2: sequential vision based\n"
    method += "3: sequential vision based with loop closure\n"

    parser.add_argument("--method", type=int, default=3, help=method)
    parser.add_argument("--output", default="output.ply", help="save PLY file")
    parser.add_argument("--width", type=int, default=640, help="image width")
    parser.add_argument("--height", type=int, default=480, help="image height")
    parser.add_argument("--min_depth", type=float, default=0.1, help="min depth distance")
    parser.add_argument("--max_depth", type=float, default=0.5, help="max depth distance")
    parser.add_argument("--max_point_dist", type=float, default=0.02, help="max distance between points for ICP/vision methods")
    parser.add_argument("--normal_radius", type=float, default=0.01, help="max radius for normal calculation for ICP methods")
    parser.add_argument("--min_matches", type=int, default=30, help="min matches for vision based method")
    parser.add_argument("--loop_closure_range", type=int, default=10, help="search N images from the start to find a loop closure with the last image")
    parser.add_argument("--uniform_color", type=int, default=0, help="use uniform color for point instead of RGB image")
    parser.add_argument("--max_vision_rmse", type=float, default=0.04, help="max rmse when estimating pose using vision")
    parser.add_argument("--mesh", type=int, default=0, help="make a mesh instead of point cloud")
    parser.add_argument("--mesh_depth", type=int, default=10, help="Poisson reconstruction depth, higher results in more detail")
    parser.add_argument("--keep_largest_mesh", type=int, default=0, help="keep only the largest mesh, useful for filtering noise")
    parser.add_argument("--view_only", type=int, default=0, help="view the data only. Hit any key to go to the next image. ESCAPE to exit.")

    args = parser.parse_args()

    process3d(args)