![](http://nghiaho.com/wp-content/uploads/2020/10/animated_mesh.png)

This is repo demonstrates how to use the iPhone TrueDepth camera as a 3D scanner. It performs automatic 3D point cloud registration and can optionally generate a 3D colored mesh. It has been tested in the simple scenario where the user pans 360 dgrees around an object and captures every 10 degrees or so.

You can check my blog post on this code at [http://nghiaho.com/?p=2629](http://nghiaho.com/?p=2629)

# Dataset
Download the test dataset and extract it somewhere
```
curl -O https://nghiaho.com/uploads/box_can.zip
```

The script expects the following directory structure
```
folder/calibration.json
folder/depthXX.bin
folder/videoXX.bin
```
To modify for your dataset edit the function process3d in process3d.py.

This dataset was provided by my friend at [https://punkoffice.com](https://punkoffice.com).

# Git submodule
Call the following to pull in the pybind11 submodule.
```
git submodule update --init --recursive
```

# Python libraries
You'll need the following Python libraries installed
- Open3D
- Numpy
- Scipy
- OpenCV
- torch
- sklearn
- pandas

All the above can be installed using pip
```
pip install open3d
pip install numpy
pip install scipy
pip install opencv-python
pip install torch
pip install sklearn
pip install pandas
```

# Compiling pose_graph.cpp
You'll need the following C++ libraries installed
- Eigen (http://eigen.tuxfamily.org/index.php?title=Main_Page)
- Ceres Solver (http://ceres-solver.org/)

On Ubuntu you can try
```
sudo apt-get install libeigen3-dev
sudo apt-get install libceres-dev
```

Compile the C++ pose graph file.
```
cd cpp
mkdir build
cd build
cmake ..
make
make install (do not run as sudo!)
```

# Running
Go back to the root folder and run

```
python3 run.py [path to test dataset]
```

For all available options
```
$ python3 run.py -h
```

# Useful options

## Tuning for your scenario
You'll want to adjust the following so your object is segmented out from the background
- --min_depth
- --max_depth

## Meshing
You can enable mesh reconstruction with --mesh 1. If you only expect a single mesh you can also use --keep_largest_mesh 1. This is useful for removing noise.

## Additional notes
```
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
```

