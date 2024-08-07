# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.

from __future__ import annotations

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric.utils import Prehashed


def _calculate_digest_and_algorithm(
    data: bytes,
    algorithm: Prehashed | hashes.HashAlgorithm,
) -> tuple[bytes, hashes.HashAlgorithm]:
    if not isinstance(algorithm, Prehashed):
        hash_ctx = hashes.Hash(algorithm)
        hash_ctx.update(data)
        data = hash_ctx.finalize()
    else:
        algorithm = algorithm._algorithm

    if len(data) != algorithm.digest_size:
        raise ValueError(
            "The provided data must be the same length as the hash "
            "algorithm's digest size."
        )

    return (data, algorithm)
