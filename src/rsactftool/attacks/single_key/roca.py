#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import logging
import subprocess
from rsactftool.lib.timeout import timeout
from rsactftool.lib.keys_wrapper import PrivateKey
from rsactftool.lib.utils import rootpath

__SAGE__ = True

logger = logging.getLogger("global_logger")


def attack(attack_rsa_obj, publickey, cipher=[]):
    try:
        sageresult = subprocess.check_output(
            ["sage", "%s/sage/roca_attack.py" %rootpath, str(publickey.n)],
            timeout=attack_rsa_obj.args.timeout,
        )

    except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
        return (None, None)

    if b"FAIL" not in sageresult and b":" in sageresult:
        sageresult = sageresult.decode("utf-8").strip()
        p, q = map(int, sageresult.split(":"))
        priv_key = PrivateKey(int(p), int(q), int(publickey.e), int(publickey.n))
        return (priv_key, None)
    else:
        return (None, None)
