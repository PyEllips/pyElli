window.BENCHMARK_DATA = {
  "lastUpdate": 1636891328571,
  "repoUrl": "https://github.com/PyEllips/pyElli",
  "entries": {
    "Python Benchmark with pytest-benchmark": [
      {
        "commit": {
          "author": {
            "email": "florian.dobener@physik.uni-giessen.de",
            "name": "Florian Dobener",
            "username": "domna"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "867bcc3d3179d958007d1e15ff6376a3a66832dd",
          "message": "Update benchmark.yml",
          "timestamp": "2021-11-13T12:53:27+01:00",
          "tree_id": "dd4579f7fc2c16b4de73e4d98ec06e142b102386",
          "url": "https://github.com/PyEllips/pyElli/commit/867bcc3d3179d958007d1e15ff6376a3a66832dd"
        },
        "date": 1636804526215,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 27.38758742830495,
            "unit": "iter/sec",
            "range": "stddev: 0.0005437723417669113",
            "extra": "mean: 36.51289119999319 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_scipy",
            "value": 1.1021593409810544,
            "unit": "iter/sec",
            "range": "stddev: 0.03882440422954798",
            "extra": "mean: 907.3098260999899 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 8.584211455602023,
            "unit": "iter/sec",
            "range": "stddev: 0.008008277684181673",
            "extra": "mean: 116.49293649999777 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 187.58978398788938,
            "unit": "iter/sec",
            "range": "stddev: 0.0001445571152863819",
            "extra": "mean: 5.330780700001014 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 238.87329391293662,
            "unit": "iter/sec",
            "range": "stddev: 0.00018414460409332144",
            "extra": "mean: 4.186319800004412 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "49639740+MarJMue@users.noreply.github.com",
            "name": "MarJMue",
            "username": "MarJMue"
          },
          "committer": {
            "email": "49639740+MarJMue@users.noreply.github.com",
            "name": "MarJMue",
            "username": "MarJMue"
          },
          "distinct": true,
          "id": "16019199a2b8424ffd938ee4b55760cc75382202",
          "message": "More documentation",
          "timestamp": "2021-11-14T12:12:06+01:00",
          "tree_id": "00b7bd09ad17b95fe84c39bd712246b5e2248739",
          "url": "https://github.com/PyEllips/pyElli/commit/16019199a2b8424ffd938ee4b55760cc75382202"
        },
        "date": 1636888476884,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 20.146364628390774,
            "unit": "iter/sec",
            "range": "stddev: 0.002442574393988315",
            "extra": "mean: 49.636746800004516 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_scipy",
            "value": 0.6929644792436743,
            "unit": "iter/sec",
            "range": "stddev: 0.03432219282524867",
            "extra": "mean: 1.4430754099999974 sec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 7.926230144855049,
            "unit": "iter/sec",
            "range": "stddev: 0.017095977275541813",
            "extra": "mean: 126.16338179999786 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 140.4277507929435,
            "unit": "iter/sec",
            "range": "stddev: 0.0002661525230456581",
            "extra": "mean: 7.121099599996228 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 147.22991551720224,
            "unit": "iter/sec",
            "range": "stddev: 0.0016658163102115044",
            "extra": "mean: 6.792097899989358 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "49639740+MarJMue@users.noreply.github.com",
            "name": "MarJMue",
            "username": "MarJMue"
          },
          "committer": {
            "email": "49639740+MarJMue@users.noreply.github.com",
            "name": "MarJMue",
            "username": "MarJMue"
          },
          "distinct": true,
          "id": "b384e92c786db02eb9785e9a348b764606747517",
          "message": "Rename function in test as well",
          "timestamp": "2021-11-14T13:00:00+01:00",
          "tree_id": "d63ec2ff69a8d07b18b656586a70a08bf54e942a",
          "url": "https://github.com/PyEllips/pyElli/commit/b384e92c786db02eb9785e9a348b764606747517"
        },
        "date": 1636891327667,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 21.258282096498707,
            "unit": "iter/sec",
            "range": "stddev: 0.0050932752339817085",
            "extra": "mean: 47.040489699998034 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_scipy",
            "value": 0.9215984025895082,
            "unit": "iter/sec",
            "range": "stddev: 0.2173732971722593",
            "extra": "mean: 1.085071325199999 sec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 10.337479164190345,
            "unit": "iter/sec",
            "range": "stddev: 0.03420582217420732",
            "extra": "mean: 96.73538240000141 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 179.72980643055254,
            "unit": "iter/sec",
            "range": "stddev: 0.0004243584537004659",
            "extra": "mean: 5.563907400002677 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 243.44021137612725,
            "unit": "iter/sec",
            "range": "stddev: 0.0002136635253079777",
            "extra": "mean: 4.107784800001468 msec\nrounds: 10"
          }
        ]
      }
    ]
  }
}