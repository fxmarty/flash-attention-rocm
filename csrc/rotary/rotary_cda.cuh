#include <torch/extension.h>
#include <c10/cuda/CUDAGuard.h>

void apply_rotary_cuda(const torch::Tensor x1, const torch::Tensor x2,
                       const torch::Tensor cos, const torch::Tensor sin,
                       torch::Tensor out1, torch::Tensor out2,
                       const bool conj);
