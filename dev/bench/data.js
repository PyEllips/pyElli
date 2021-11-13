window.BENCHMARK_DATA = {
  "lastUpdate": 1636804527012,
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
      }
    ]
  }
}