
cmake_minimum_required(VERSION 2.8)


project(sod)
add_library (${PROJECT_NAME} sod.c )

add_definitions(-DSOD_ENABLE_NET_TRAIN)
############ Gen By Python Script ############

cmake_minimum_required(VERSION 2.8)

# include
INCLUDE_DIRECTORIES(${CMAKE_CURRENT_LIST_DIR})

# MT MTd
set(CMAKE_C_FLAGS_DEBUG "${CMAKE_C_FLAGS_DEBUG} /MTd")
set(CMAKE_C_FLAGS_RELEASE "${CMAKE_C_FLAGS_RELEASE} /MT")

set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} /MTd")
set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} /MT")

if (MSVC)
    set(CompilerFlags
        CMAKE_CXX_FLAGS
        CMAKE_CXX_FLAGS_DEBUG
        CMAKE_CXX_FLAGS_RELEASE
        CMAKE_C_FLAGS
        CMAKE_C_FLAGS_DEBUG
        CMAKE_C_FLAGS_RELEASE
        )
    foreach(CompilerFlag ${CompilerFlags})
        string(REPLACE "/MD" "/MT" ${CompilerFlag} "${${CompilerFlag}}")
    endforeach()
endif(MSVC)


# link lib
target_link_libraries(${PROJECT_NAME}
 # ws2_32.lib
  #psapi.lib
  #iphlpapi.lib
  # debug lib
  #debug  ${CMAKE_CURRENT_LIST_DIR}/../../libuv/Debug/lib/libuv.lib
  # release lib
  #optimized   ${CMAKE_CURRENT_LIST_DIR}/../../libuv/Release/lib/libuv.lib
)



include_directories(${CMAKE_CURRENT_LIST_DIR})

add_subdirectory(samples/batch_img_loading)
add_subdirectory(samples/blob_detection)
add_subdirectory(samples/canny_edge_detection)
add_subdirectory(samples/cnn_coco)
add_subdirectory(samples/cnn_face_detection)
add_subdirectory(samples/cnn_object_detection)
add_subdirectory(samples/cnn_voc)
add_subdirectory(samples/crop_image)
add_subdirectory(samples/dilate_image)
add_subdirectory(samples/erode_image)
add_subdirectory(samples/grayscale_image)
add_subdirectory(samples/hilditch_thin)
add_subdirectory(samples/hough_lines_detection)
add_subdirectory(samples/license_plate_detection)
add_subdirectory(samples/otsu_image)
add_subdirectory(samples/realnet_face_detection)
add_subdirectory(samples/realnet_train_model)
add_subdirectory(samples/resize_image)
add_subdirectory(samples/rnn_text_gen)
add_subdirectory(samples/rotate_image)
add_subdirectory(samples/sobel_operator_img)



