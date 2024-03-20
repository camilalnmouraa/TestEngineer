# Test Automation Engineer

This test aims to demonstrate your abilities to write and execute a simple testing framework under the GitHub CI/CD runners. The included repository has a single Python file with several functions inside that require basic tests. You can use any framework you are familiar with to write tests for these functions.

- Write tests for each function inside the Python file.
- Push the code and your tests to a GitHub repository, and write a GitHub workflow that should:
  - Execute tests against that image.
  - Bonus points for building a containerized docker image and executing the tests against that image.

---

## Test Checklist

### obj_rect2coords Function

- [x] Verify if the function returns correct coordinates for a rectangular object.
- [x] Test with standard rectangular object.
- [x] Test with additional rectangular object.

### compute_affine Function

- [x] Verify if the function correctly calculates an affine transformation.
- [x] Test with standard rectangular object and standard frame transformation matrix.
- [x] Test with additional rectangular object and additional frame transformation matrix.

### draw_edge_locs Function

- [x] Verify if the function correctly draws edges on the image.
- [x] Test with standard edge locations and standard color.
- [x] Test with additional edge locations and additional colors.

### hex2bgr Function

- [x] Verify if the function converts hexadecimal color to BGR correctly.
- [x] Test with standard hexadecimal color.
- [x] Test with additional hexadecimal colors.

### bgr2hex Function

- [x] Verify if the function converts BGR color to hexadecimal correctly.
- [x] Test with standard BGR color.
- [x] Test with additional BGR colors.

### is_port_open Function

- [x] Verify if the function detects whether a port is open or closed correctly.
- [x] Test with open port.
- [x] Test with closed port.

### wait_for_service Function

- [x] Verify if the function waits until a service is available correctly.