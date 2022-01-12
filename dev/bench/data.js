window.BENCHMARK_DATA = {
  "lastUpdate": 1642020140716,
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
          "id": "76b451ce849536010540b9613745cdb9b8392648",
          "message": "Documentation",
          "timestamp": "2021-11-14T20:43:45+01:00",
          "tree_id": "af2c4d261dd4bf2b61894ae1aa54e25f95b70747",
          "url": "https://github.com/PyEllips/pyElli/commit/76b451ce849536010540b9613745cdb9b8392648"
        },
        "date": 1636919151352,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 24.009813559907904,
            "unit": "iter/sec",
            "range": "stddev: 0.0017059483115295687",
            "extra": "mean: 41.64963620000037 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_scipy",
            "value": 1.0133221486185249,
            "unit": "iter/sec",
            "range": "stddev: 0.03571425854602444",
            "extra": "mean: 986.8529977000037 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 9.413724559165253,
            "unit": "iter/sec",
            "range": "stddev: 0.02415843243070432",
            "extra": "mean: 106.22787970000616 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 182.77043238629918,
            "unit": "iter/sec",
            "range": "stddev: 0.000264132751074497",
            "extra": "mean: 5.471344500003283 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 234.42942608830145,
            "unit": "iter/sec",
            "range": "stddev: 0.000330845507802948",
            "extra": "mean: 4.265676099993243 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "49639740+MarJMue@users.noreply.github.com",
            "name": "Marius Müller",
            "username": "MarJMue"
          },
          "committer": {
            "email": "49639740+MarJMue@users.noreply.github.com",
            "name": "Marius Müller",
            "username": "MarJMue"
          },
          "distinct": true,
          "id": "dd2acbfd56997b2865afa6f1bffe74ba73f2f667",
          "message": "Structure and Layer documentation",
          "timestamp": "2021-11-15T10:27:32+01:00",
          "tree_id": "72eda4ae466b4bd65947e6ae067bc9c5f2fd1643",
          "url": "https://github.com/PyEllips/pyElli/commit/dd2acbfd56997b2865afa6f1bffe74ba73f2f667"
        },
        "date": 1636968571583,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 24.926441945189662,
            "unit": "iter/sec",
            "range": "stddev: 0.00036091614048225167",
            "extra": "mean: 40.118040199996585 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_scipy",
            "value": 1.0956475180913479,
            "unit": "iter/sec",
            "range": "stddev: 0.02626852884438932",
            "extra": "mean: 912.7022910999983 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 9.175637637883968,
            "unit": "iter/sec",
            "range": "stddev: 0.013343505631910458",
            "extra": "mean: 108.98425149999866 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 172.7660571365868,
            "unit": "iter/sec",
            "range": "stddev: 0.0001648049725672274",
            "extra": "mean: 5.7881739999970705 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 222.2124695635994,
            "unit": "iter/sec",
            "range": "stddev: 0.00009367835147340736",
            "extra": "mean: 4.500197500004788 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "49639740+MarJMue@users.noreply.github.com",
            "name": "Marius Müller",
            "username": "MarJMue"
          },
          "committer": {
            "email": "49639740+MarJMue@users.noreply.github.com",
            "name": "Marius Müller",
            "username": "MarJMue"
          },
          "distinct": true,
          "id": "08fae4f936c4fd13ec834775d8ba5501aaf1fe25",
          "message": "More cleaning",
          "timestamp": "2021-11-15T10:27:55+01:00",
          "tree_id": "fc9551e51a2d45a1841db63d6f455572eaae6887",
          "url": "https://github.com/PyEllips/pyElli/commit/08fae4f936c4fd13ec834775d8ba5501aaf1fe25"
        },
        "date": 1636968597667,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 26.252667766560645,
            "unit": "iter/sec",
            "range": "stddev: 0.000947557705421821",
            "extra": "mean: 38.09136690000514 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_scipy",
            "value": 1.1059152506828098,
            "unit": "iter/sec",
            "range": "stddev: 0.014534283566777528",
            "extra": "mean: 904.2284201999962 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 8.55493369134291,
            "unit": "iter/sec",
            "range": "stddev: 0.008818515973319787",
            "extra": "mean: 116.89161319998789 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 194.03940820091054,
            "unit": "iter/sec",
            "range": "stddev: 0.00008567590341974543",
            "extra": "mean: 5.153592299996035 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 245.9978971108154,
            "unit": "iter/sec",
            "range": "stddev: 0.00026819531854225956",
            "extra": "mean: 4.065075400012574 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "49639740+MarJMue@users.noreply.github.com",
            "name": "Marius Müller",
            "username": "MarJMue"
          },
          "committer": {
            "email": "49639740+MarJMue@users.noreply.github.com",
            "name": "Marius Müller",
            "username": "MarJMue"
          },
          "distinct": true,
          "id": "9f61f276425cc3370c80a720bfd2da11885e6300",
          "message": "Update change-log and readme",
          "timestamp": "2021-11-15T10:50:23+01:00",
          "tree_id": "c4fa84ca873a69a1aca4469f2aede93c3dc3b9ad",
          "url": "https://github.com/PyEllips/pyElli/commit/9f61f276425cc3370c80a720bfd2da11885e6300"
        },
        "date": 1636969944108,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 25.327771631605742,
            "unit": "iter/sec",
            "range": "stddev: 0.0006647114251386826",
            "extra": "mean: 39.482352199991055 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_scipy",
            "value": 1.157986895277916,
            "unit": "iter/sec",
            "range": "stddev: 0.025008232142050044",
            "extra": "mean: 863.5676311000054 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 9.178275889235127,
            "unit": "iter/sec",
            "range": "stddev: 0.013605075989374122",
            "extra": "mean: 108.95292449999943 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 196.18320474405428,
            "unit": "iter/sec",
            "range": "stddev: 0.00011252879274959164",
            "extra": "mean: 5.097276300000431 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 260.7018228633875,
            "unit": "iter/sec",
            "range": "stddev: 0.00014076696087214489",
            "extra": "mean: 3.8357998000037696 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "49639740+MarJMue@users.noreply.github.com",
            "name": "Marius Müller",
            "username": "MarJMue"
          },
          "committer": {
            "email": "49639740+MarJMue@users.noreply.github.com",
            "name": "Marius Müller",
            "username": "MarJMue"
          },
          "distinct": true,
          "id": "d8602f811af3d76db704e1b0f5dc5d32d5198ca2",
          "message": "Mention tmm",
          "timestamp": "2021-11-15T10:59:37+01:00",
          "tree_id": "d0cebeb1a626c53e054b94aa91781a65eb6ed195",
          "url": "https://github.com/PyEllips/pyElli/commit/d8602f811af3d76db704e1b0f5dc5d32d5198ca2"
        },
        "date": 1636970496250,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 25.148200293316666,
            "unit": "iter/sec",
            "range": "stddev: 0.0012999037987605992",
            "extra": "mean: 39.76427689999582 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_scipy",
            "value": 1.089119372885514,
            "unit": "iter/sec",
            "range": "stddev: 0.024140306346260916",
            "extra": "mean: 918.1729982000036 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 9.32873083605872,
            "unit": "iter/sec",
            "range": "stddev: 0.017912910856447976",
            "extra": "mean: 107.19571799999414 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 189.92769737451763,
            "unit": "iter/sec",
            "range": "stddev: 0.00011640656535877162",
            "extra": "mean: 5.265161500000204 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 249.66579113030855,
            "unit": "iter/sec",
            "range": "stddev: 0.0001241673405867077",
            "extra": "mean: 4.005354500000635 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "49639740+MarJMue@users.noreply.github.com",
            "name": "Marius Müller",
            "username": "MarJMue"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "4fd429cce2689eeece18c8d93f9d56f521cea843",
          "message": "Include DOI badge",
          "timestamp": "2021-11-15T11:07:07+01:00",
          "tree_id": "4c69c61cadc909d232f3f3bcca755f09ba1de13b",
          "url": "https://github.com/PyEllips/pyElli/commit/4fd429cce2689eeece18c8d93f9d56f521cea843"
        },
        "date": 1636970972624,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 19.25745094752719,
            "unit": "iter/sec",
            "range": "stddev: 0.0009863512790469642",
            "extra": "mean: 51.92795259999912 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_scipy",
            "value": 0.6657202912162156,
            "unit": "iter/sec",
            "range": "stddev: 0.028906658678392726",
            "extra": "mean: 1.502132371799999 sec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 11.359471452154361,
            "unit": "iter/sec",
            "range": "stddev: 0.04314587385727499",
            "extra": "mean: 88.03226489999645 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 129.67119909433575,
            "unit": "iter/sec",
            "range": "stddev: 0.00022780421413627172",
            "extra": "mean: 7.711812700000564 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 171.7763724486968,
            "unit": "iter/sec",
            "range": "stddev: 0.00010721641019319831",
            "extra": "mean: 5.82152239999516 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "49639740+MarJMue@users.noreply.github.com",
            "name": "Marius Müller",
            "username": "MarJMue"
          },
          "committer": {
            "email": "49639740+MarJMue@users.noreply.github.com",
            "name": "Marius Müller",
            "username": "MarJMue"
          },
          "distinct": true,
          "id": "ebbd9079797e828e0ca5373c8fc0b3991fe1b38b",
          "message": "Create .zenodo.json",
          "timestamp": "2021-11-15T11:54:33+01:00",
          "tree_id": "6181cf7cdac3e5be501969de17f7386e466031ee",
          "url": "https://github.com/PyEllips/pyElli/commit/ebbd9079797e828e0ca5373c8fc0b3991fe1b38b"
        },
        "date": 1636973793397,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 25.75325343297158,
            "unit": "iter/sec",
            "range": "stddev: 0.0003470374534805198",
            "extra": "mean: 38.8300454000003 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_scipy",
            "value": 1.128505824149266,
            "unit": "iter/sec",
            "range": "stddev: 0.01721070710700149",
            "extra": "mean: 886.1274604000016 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 9.06914631395668,
            "unit": "iter/sec",
            "range": "stddev: 0.028641869550976983",
            "extra": "mean: 110.26396150000153 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 196.9708910309219,
            "unit": "iter/sec",
            "range": "stddev: 0.0004260839755977873",
            "extra": "mean: 5.076892300004943 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 245.00259029000486,
            "unit": "iter/sec",
            "range": "stddev: 0.00009761464406021144",
            "extra": "mean: 4.081589499998017 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "49639740+MarJMue@users.noreply.github.com",
            "name": "Marius Müller",
            "username": "MarJMue"
          },
          "committer": {
            "email": "49639740+MarJMue@users.noreply.github.com",
            "name": "Marius Müller",
            "username": "MarJMue"
          },
          "distinct": true,
          "id": "1484d35ec7a6b8f865355798a7d82cec1f95ae65",
          "message": "Update .zenodo.json",
          "timestamp": "2021-11-15T11:58:16+01:00",
          "tree_id": "f6f0a4213aeee50af4b887684b6157494e5a51a7",
          "url": "https://github.com/PyEllips/pyElli/commit/1484d35ec7a6b8f865355798a7d82cec1f95ae65"
        },
        "date": 1636974013168,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 26.02488061866753,
            "unit": "iter/sec",
            "range": "stddev: 0.0009725805317611923",
            "extra": "mean: 38.42476800000014 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_scipy",
            "value": 1.0916256475202815,
            "unit": "iter/sec",
            "range": "stddev: 0.018634110672395527",
            "extra": "mean: 916.0649552999998 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 9.577226788981633,
            "unit": "iter/sec",
            "range": "stddev: 0.015456217520882293",
            "extra": "mean: 104.41435939999621 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 192.23922556816126,
            "unit": "iter/sec",
            "range": "stddev: 0.0001019806212710583",
            "extra": "mean: 5.201851999999008 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 251.11674756588658,
            "unit": "iter/sec",
            "range": "stddev: 0.00010865810529476462",
            "extra": "mean: 3.9822115000021086 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "49639740+MarJMue@users.noreply.github.com",
            "name": "Marius Müller",
            "username": "MarJMue"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "a782e36f05e8c1403ddf94919b75af73abcbeca0",
          "message": "Update DOI",
          "timestamp": "2021-11-15T12:28:22+01:00",
          "tree_id": "424d0fdccb8f40817a48949e51796e51e2ad2605",
          "url": "https://github.com/PyEllips/pyElli/commit/a782e36f05e8c1403ddf94919b75af73abcbeca0"
        },
        "date": 1636975821833,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 25.693777205599925,
            "unit": "iter/sec",
            "range": "stddev: 0.00126561867928785",
            "extra": "mean: 38.91992959999868 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_scipy",
            "value": 1.0657970208621748,
            "unit": "iter/sec",
            "range": "stddev: 0.02652296828947435",
            "extra": "mean: 938.2649607999952 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 9.17890925488388,
            "unit": "iter/sec",
            "range": "stddev: 0.012058456113756437",
            "extra": "mean: 108.94540650000692 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 187.50168517143067,
            "unit": "iter/sec",
            "range": "stddev: 0.0002689176559044659",
            "extra": "mean: 5.333285399998999 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 245.52952727049626,
            "unit": "iter/sec",
            "range": "stddev: 0.00011209434180937396",
            "extra": "mean: 4.0728298999994195 msec\nrounds: 10"
          }
        ]
      },
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
          "id": "a38ed787fa73860149cee3790e506de916fd0078",
          "message": "Update README.md",
          "timestamp": "2021-11-15T12:46:51+01:00",
          "tree_id": "21508773e93725c5f4c7802e835e16362dac9628",
          "url": "https://github.com/PyEllips/pyElli/commit/a38ed787fa73860149cee3790e506de916fd0078"
        },
        "date": 1636976928540,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 22.595470114832345,
            "unit": "iter/sec",
            "range": "stddev: 0.005635721324138349",
            "extra": "mean: 44.25665830000014 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_scipy",
            "value": 1.0939718309756064,
            "unit": "iter/sec",
            "range": "stddev: 0.019144007773764654",
            "extra": "mean: 914.1003192999932 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 8.817262464668511,
            "unit": "iter/sec",
            "range": "stddev: 0.009493840049677117",
            "extra": "mean: 113.41388600000073 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 192.1599841013494,
            "unit": "iter/sec",
            "range": "stddev: 0.00010729382286911065",
            "extra": "mean: 5.203997100002766 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 252.26254274583192,
            "unit": "iter/sec",
            "range": "stddev: 0.00006923659405767714",
            "extra": "mean: 3.964124000000879 msec\nrounds: 10"
          }
        ]
      },
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
          "id": "b844ce62848ce9215e68d07ebd0b2afce165dc0a",
          "message": "Update README.md",
          "timestamp": "2021-11-15T17:09:54+01:00",
          "tree_id": "07d296f135e860fd440fa4cac8f14929be59b28a",
          "url": "https://github.com/PyEllips/pyElli/commit/b844ce62848ce9215e68d07ebd0b2afce165dc0a"
        },
        "date": 1636992715346,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 25.52147220224332,
            "unit": "iter/sec",
            "range": "stddev: 0.0004295463077724406",
            "extra": "mean: 39.182692600002156 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_scipy",
            "value": 1.0946315240067273,
            "unit": "iter/sec",
            "range": "stddev: 0.019002653069319756",
            "extra": "mean: 913.5494256000015 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 8.953708493498505,
            "unit": "iter/sec",
            "range": "stddev: 0.01408167586269032",
            "extra": "mean: 111.6855658999981 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 181.25411242917136,
            "unit": "iter/sec",
            "range": "stddev: 0.00022809445334657282",
            "extra": "mean: 5.517116200002192 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 248.65459216517127,
            "unit": "iter/sec",
            "range": "stddev: 0.0000966032227494544",
            "extra": "mean: 4.02164300000436 msec\nrounds: 10"
          }
        ]
      },
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
          "id": "353e8629e295cd08f14fc8a80285032c317a2bc3",
          "message": "Update setup.cfg",
          "timestamp": "2021-11-15T17:12:55+01:00",
          "tree_id": "d943c3f3ef7d79f1254d109eee3541e15827f2a5",
          "url": "https://github.com/PyEllips/pyElli/commit/353e8629e295cd08f14fc8a80285032c317a2bc3"
        },
        "date": 1636992886113,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 27.347311869864804,
            "unit": "iter/sec",
            "range": "stddev: 0.0007272042664308852",
            "extra": "mean: 36.56666529999768 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_scipy",
            "value": 1.1713165418953755,
            "unit": "iter/sec",
            "range": "stddev: 0.03168645771968143",
            "extra": "mean: 853.7401839999987 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 9.211946879209277,
            "unit": "iter/sec",
            "range": "stddev: 0.014823290962113852",
            "extra": "mean: 108.55468589999475 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 197.0684219786564,
            "unit": "iter/sec",
            "range": "stddev: 0.0001672509071566392",
            "extra": "mean: 5.074379700002396 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 263.94263787439996,
            "unit": "iter/sec",
            "range": "stddev: 0.00008496569805585854",
            "extra": "mean: 3.788701999999944 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "github@schroedingerscat.org",
            "name": "domna",
            "username": "domna"
          },
          "committer": {
            "email": "github@schroedingerscat.org",
            "name": "domna",
            "username": "domna"
          },
          "distinct": true,
          "id": "7d07e84688164a4290036b0a3385a78ccf6bc1a1",
          "message": "Sets sphinx's autoclass_content to both",
          "timestamp": "2021-11-16T19:52:34+01:00",
          "tree_id": "cdb3744cfa46f646269298af36a94693eec6c8f3",
          "url": "https://github.com/PyEllips/pyElli/commit/7d07e84688164a4290036b0a3385a78ccf6bc1a1"
        },
        "date": 1637088887562,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 24.21738540330824,
            "unit": "iter/sec",
            "range": "stddev: 0.0012115281786618066",
            "extra": "mean: 41.29264919999969 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_scipy",
            "value": 1.0460941598385325,
            "unit": "iter/sec",
            "range": "stddev: 0.036698922270012056",
            "extra": "mean: 955.936892099993 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 8.408517270678107,
            "unit": "iter/sec",
            "range": "stddev: 0.01958516649898217",
            "extra": "mean: 118.927031700008 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 171.68510232742037,
            "unit": "iter/sec",
            "range": "stddev: 0.0002117203286724197",
            "extra": "mean: 5.824617199999693 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 240.5196127989396,
            "unit": "iter/sec",
            "range": "stddev: 0.0003447638275932423",
            "extra": "mean: 4.157665100001395 msec\nrounds: 10"
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
          "id": "f83e469c35b959ff032422f8ba8cb87a0a2d6991",
          "message": "Material documentation",
          "timestamp": "2021-11-22T11:53:00+01:00",
          "tree_id": "9e99f02690b2da53e4fe8d1be60f0f21d8594262",
          "url": "https://github.com/PyEllips/pyElli/commit/f83e469c35b959ff032422f8ba8cb87a0a2d6991"
        },
        "date": 1637578533744,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 18.46357710178071,
            "unit": "iter/sec",
            "range": "stddev: 0.0012459313776081932",
            "extra": "mean: 54.160685900001226 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_scipy",
            "value": 0.6129629102403218,
            "unit": "iter/sec",
            "range": "stddev: 0.055971512007329",
            "extra": "mean: 1.6314200798999963 sec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 8.627781401412093,
            "unit": "iter/sec",
            "range": "stddev: 0.041519919673929706",
            "extra": "mean: 115.9046519000043 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 129.8994702804814,
            "unit": "iter/sec",
            "range": "stddev: 0.0001838282682444792",
            "extra": "mean: 7.69826079999234 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 167.6058010781985,
            "unit": "iter/sec",
            "range": "stddev: 0.00024553502995825453",
            "extra": "mean: 5.966380599997478 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "49639740+MarJMue@users.noreply.github.com",
            "name": "Marius Müller",
            "username": "MarJMue"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "79f52e24a467887ddf70a5c771e1b6294869a937",
          "message": "Merge pull request #35 from PyEllips/decorators\n\n- Added Fit, Undo and Redo Button for fitting decorators\r\n- Added decorators base class\r\n- Refactored Psi/Delta convention to -pi/pi for SpectraRay files",
          "timestamp": "2021-11-22T14:50:18+01:00",
          "tree_id": "5fd31972775557c67b51ddc68a905b0a18bf0f70",
          "url": "https://github.com/PyEllips/pyElli/commit/79f52e24a467887ddf70a5c771e1b6294869a937"
        },
        "date": 1637589144845,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 25.177389944484148,
            "unit": "iter/sec",
            "range": "stddev: 0.0008431719311804359",
            "extra": "mean: 39.718175799993105 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_scipy",
            "value": 1.089300690312564,
            "unit": "iter/sec",
            "range": "stddev: 0.025651833295619708",
            "extra": "mean: 918.0201654999962 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 9.46961087335771,
            "unit": "iter/sec",
            "range": "stddev: 0.02494439749394592",
            "extra": "mean: 105.6009601000028 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 187.28447770502277,
            "unit": "iter/sec",
            "range": "stddev: 0.00022999931083580614",
            "extra": "mean: 5.339470800004165 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 249.45895470993082,
            "unit": "iter/sec",
            "range": "stddev: 0.00009312048343392859",
            "extra": "mean: 4.008675499994752 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "florian.dobener@physik.uni-giessen.de",
            "name": "dobener",
            "username": "domna"
          },
          "committer": {
            "email": "florian.dobener@physik.uni-giessen.de",
            "name": "dobener",
            "username": "domna"
          },
          "distinct": true,
          "id": "7a21cc0bcdfed5f40d68efbbad2cc72330a2f3b8",
          "message": "Adds export functions for decorators (fixes #36)",
          "timestamp": "2021-11-23T12:37:27+01:00",
          "tree_id": "333e2001cc413c8bed5326e52458cbb48df3f399",
          "url": "https://github.com/PyEllips/pyElli/commit/7a21cc0bcdfed5f40d68efbbad2cc72330a2f3b8"
        },
        "date": 1637667575501,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 24.90551935573031,
            "unit": "iter/sec",
            "range": "stddev: 0.0005743921088727533",
            "extra": "mean: 40.15174249999802 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_scipy",
            "value": 1.100920455956462,
            "unit": "iter/sec",
            "range": "stddev: 0.014259150607650959",
            "extra": "mean: 908.3308377000009 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 9.03891602976101,
            "unit": "iter/sec",
            "range": "stddev: 0.014660591070049158",
            "extra": "mean: 110.63273479999793 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 190.8948574416071,
            "unit": "iter/sec",
            "range": "stddev: 0.00014134167044648177",
            "extra": "mean: 5.238485799995374 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 249.50513774794172,
            "unit": "iter/sec",
            "range": "stddev: 0.00009161196442198142",
            "extra": "mean: 4.007933499991623 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "49639740+MarJMue@users.noreply.github.com",
            "name": "Marius Müller",
            "username": "MarJMue"
          },
          "committer": {
            "email": "49639740+MarJMue@users.noreply.github.com",
            "name": "Marius Müller",
            "username": "MarJMue"
          },
          "distinct": true,
          "id": "73c777699780d7ef3c037293bf094caa686b6792",
          "message": "Prepare version 0.9.2",
          "timestamp": "2021-11-23T14:33:50+01:00",
          "tree_id": "a67b244f1c775aab1cd2dce88e58d9f984e69b5a",
          "url": "https://github.com/PyEllips/pyElli/commit/73c777699780d7ef3c037293bf094caa686b6792"
        },
        "date": 1637674582641,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 21.631259013987545,
            "unit": "iter/sec",
            "range": "stddev: 0.0007169328520353324",
            "extra": "mean: 46.22939420000307 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_scipy",
            "value": 0.9310038803913984,
            "unit": "iter/sec",
            "range": "stddev: 0.02432573659509155",
            "extra": "mean: 1.0741093792000043 sec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 8.732443637104197,
            "unit": "iter/sec",
            "range": "stddev: 0.023885858826148878",
            "extra": "mean: 114.51548289999778 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 153.32218353976089,
            "unit": "iter/sec",
            "range": "stddev: 0.000270070831288702",
            "extra": "mean: 6.522213399998122 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 200.84544685774316,
            "unit": "iter/sec",
            "range": "stddev: 0.00019857682523263202",
            "extra": "mean: 4.9789528000019345 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "florian.dobener@physik.uni-giessen.de",
            "name": "dobener",
            "username": "domna"
          },
          "committer": {
            "email": "florian.dobener@physik.uni-giessen.de",
            "name": "dobener",
            "username": "domna"
          },
          "distinct": true,
          "id": "a0fd655e384d263837b6f8b3eb303769c3ac521e",
          "message": "Adds fitting checkboxes for decorators (fixes #37)",
          "timestamp": "2021-11-24T13:43:16+01:00",
          "tree_id": "c93d15d8c4da7700d02f94708f386e78eb54983d",
          "url": "https://github.com/PyEllips/pyElli/commit/a0fd655e384d263837b6f8b3eb303769c3ac521e"
        },
        "date": 1637757973998,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 18.077155886356497,
            "unit": "iter/sec",
            "range": "stddev: 0.0031102531678532937",
            "extra": "mean: 55.31843649999928 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_scipy",
            "value": 0.6232165637899533,
            "unit": "iter/sec",
            "range": "stddev: 0.045822841805320896",
            "extra": "mean: 1.604578661900001 sec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 8.362635324561797,
            "unit": "iter/sec",
            "range": "stddev: 0.025988116074589538",
            "extra": "mean: 119.57952980000357 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 126.56271252648216,
            "unit": "iter/sec",
            "range": "stddev: 0.0008633629698060536",
            "extra": "mean: 7.901221299999862 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 167.10619774333816,
            "unit": "iter/sec",
            "range": "stddev: 0.00023761489288624094",
            "extra": "mean: 5.984218499997951 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "florian.dobener@physik.uni-giessen.de",
            "name": "dobener",
            "username": "domna"
          },
          "committer": {
            "email": "florian.dobener@physik.uni-giessen.de",
            "name": "dobener",
            "username": "domna"
          },
          "distinct": true,
          "id": "069ccb2205ba27e07b41b6e067f1442fbd4d7e69",
          "message": "Adds residual display to decorators (fixes #39)",
          "timestamp": "2021-11-24T14:20:42+01:00",
          "tree_id": "ca85ac5b0c1695e8778f5bc75e28c137d164d6f5",
          "url": "https://github.com/PyEllips/pyElli/commit/069ccb2205ba27e07b41b6e067f1442fbd4d7e69"
        },
        "date": 1637760180723,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 23.921216583130427,
            "unit": "iter/sec",
            "range": "stddev: 0.0011773254503053203",
            "extra": "mean: 41.803893899995614 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_scipy",
            "value": 1.0122917063904888,
            "unit": "iter/sec",
            "range": "stddev: 0.023099099245945817",
            "extra": "mean: 987.8575451000017 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 8.49396445769023,
            "unit": "iter/sec",
            "range": "stddev: 0.026846267413799803",
            "extra": "mean: 117.73065510000151 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 184.06642942712207,
            "unit": "iter/sec",
            "range": "stddev: 0.0004906995033274494",
            "extra": "mean: 5.432821200000149 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 220.40692142976988,
            "unit": "iter/sec",
            "range": "stddev: 0.00022170903971183926",
            "extra": "mean: 4.537062599999331 msec\nrounds: 10"
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
          "id": "8de4d82fa2f6ddf5f4fab7f443b4a1b01d956650",
          "message": "Fix examples and Structure plotting",
          "timestamp": "2021-11-26T07:26:58+01:00",
          "tree_id": "45fe4281db75aa243cede0e4689430cdb6e4a080",
          "url": "https://github.com/PyEllips/pyElli/commit/8de4d82fa2f6ddf5f4fab7f443b4a1b01d956650"
        },
        "date": 1637908155951,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 26.82183987946109,
            "unit": "iter/sec",
            "range": "stddev: 0.0007952633173240325",
            "extra": "mean: 37.28305009999531 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_scipy",
            "value": 1.1060564105791622,
            "unit": "iter/sec",
            "range": "stddev: 0.04187940096163273",
            "extra": "mean: 904.1130184999986 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 9.801868759409539,
            "unit": "iter/sec",
            "range": "stddev: 0.0219255350014872",
            "extra": "mean: 102.02136189999749 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 175.10094350513128,
            "unit": "iter/sec",
            "range": "stddev: 0.00013694093701100028",
            "extra": "mean: 5.710991500001228 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 234.04770622434523,
            "unit": "iter/sec",
            "range": "stddev: 0.00012155901038000897",
            "extra": "mean: 4.272633200008613 msec\nrounds: 10"
          }
        ]
      },
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
          "id": "8d3d02a5f22cfccedd873011307c86ffb2c3eb2f",
          "message": "Merge pull request #40 from PyEllips/result-rewrite\n\nResult rewrite",
          "timestamp": "2021-11-30T12:27:32+01:00",
          "tree_id": "c20408a4904b712266f2a57bbc1c35d73c08bb9c",
          "url": "https://github.com/PyEllips/pyElli/commit/8d3d02a5f22cfccedd873011307c86ffb2c3eb2f"
        },
        "date": 1638271773296,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 25.30559408676866,
            "unit": "iter/sec",
            "range": "stddev: 0.0005795524903550413",
            "extra": "mean: 39.51695409999729 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_scipy",
            "value": 1.0838782995926386,
            "unit": "iter/sec",
            "range": "stddev: 0.02253794832921243",
            "extra": "mean: 922.6128066000001 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 8.26068582637387,
            "unit": "iter/sec",
            "range": "stddev: 0.007261157206458908",
            "extra": "mean: 121.05532410000421 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 152.63493225651206,
            "unit": "iter/sec",
            "range": "stddev: 0.00014805929010668387",
            "extra": "mean: 6.551580199999307 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 189.07556550570033,
            "unit": "iter/sec",
            "range": "stddev: 0.0001065385478195715",
            "extra": "mean: 5.2888906999982055 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "49639740+MarJMue@users.noreply.github.com",
            "name": "Marius Müller",
            "username": "MarJMue"
          },
          "committer": {
            "email": "49639740+MarJMue@users.noreply.github.com",
            "name": "Marius Müller",
            "username": "MarJMue"
          },
          "distinct": true,
          "id": "7716ee6f21867ea42c957658bf3c2b3a97421bbc",
          "message": "Fix mueller matrix calculation",
          "timestamp": "2021-12-01T11:23:57+01:00",
          "tree_id": "62cc02fb4f3fb9bf2c04758c4e7d9fafd812764d",
          "url": "https://github.com/PyEllips/pyElli/commit/7716ee6f21867ea42c957658bf3c2b3a97421bbc"
        },
        "date": 1638354367725,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 24.852942591264235,
            "unit": "iter/sec",
            "range": "stddev: 0.001049568832317662",
            "extra": "mean: 40.23668409999459 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_scipy",
            "value": 1.076501594882986,
            "unit": "iter/sec",
            "range": "stddev: 0.022916691120402705",
            "extra": "mean: 928.9349915999878 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 8.500865709887728,
            "unit": "iter/sec",
            "range": "stddev: 0.010843675025628417",
            "extra": "mean: 117.63507789999039 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 157.87137104856183,
            "unit": "iter/sec",
            "range": "stddev: 0.0001890367857013001",
            "extra": "mean: 6.33427069998902 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 192.00368401338199,
            "unit": "iter/sec",
            "range": "stddev: 0.00009819363964130562",
            "extra": "mean: 5.208233399991968 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "49639740+MarJMue@users.noreply.github.com",
            "name": "Marius Müller",
            "username": "MarJMue"
          },
          "committer": {
            "email": "49639740+MarJMue@users.noreply.github.com",
            "name": "Marius Müller",
            "username": "MarJMue"
          },
          "distinct": true,
          "id": "9ae593377c1629aaa7e19aab67f46d1bb9c826fb",
          "message": "Fix Result getattr",
          "timestamp": "2021-12-02T09:30:02+01:00",
          "tree_id": "f1ec0d6111adf49e0ba7967359f12981366a9f60",
          "url": "https://github.com/PyEllips/pyElli/commit/9ae593377c1629aaa7e19aab67f46d1bb9c826fb"
        },
        "date": 1638434003715,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 25.143155446999614,
            "unit": "iter/sec",
            "range": "stddev: 0.0003329056700746025",
            "extra": "mean: 39.7722554000012 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_scipy",
            "value": 1.12283064221575,
            "unit": "iter/sec",
            "range": "stddev: 0.021871071852530365",
            "extra": "mean: 890.6062610000021 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 10.635100949680808,
            "unit": "iter/sec",
            "range": "stddev: 0.033313525872665985",
            "extra": "mean: 94.02825650000182 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 162.42886772898183,
            "unit": "iter/sec",
            "range": "stddev: 0.00016452368451123372",
            "extra": "mean: 6.156541100000368 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 191.19504743655793,
            "unit": "iter/sec",
            "range": "stddev: 0.00008247006610279553",
            "extra": "mean: 5.230260999996972 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "49639740+MarJMue@users.noreply.github.com",
            "name": "Marius Müller",
            "username": "MarJMue"
          },
          "committer": {
            "email": "49639740+MarJMue@users.noreply.github.com",
            "name": "Marius Müller",
            "username": "MarJMue"
          },
          "distinct": true,
          "id": "9ef1b86ad6c3a4280dccc751ed56a9d29716b49b",
          "message": "Framework to handle multiple Results at once (fixes #41)",
          "timestamp": "2021-12-02T09:32:47+01:00",
          "tree_id": "ef1311b4c5f47e462043e41ee7c5d3237d01eb63",
          "url": "https://github.com/PyEllips/pyElli/commit/9ef1b86ad6c3a4280dccc751ed56a9d29716b49b"
        },
        "date": 1638434096407,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 24.859978100000763,
            "unit": "iter/sec",
            "range": "stddev: 0.0008895227749946845",
            "extra": "mean: 40.22529689999885 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_scipy",
            "value": 1.093049630430454,
            "unit": "iter/sec",
            "range": "stddev: 0.021455929613340165",
            "extra": "mean: 914.8715412000001 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 9.279868412059745,
            "unit": "iter/sec",
            "range": "stddev: 0.016656437732166504",
            "extra": "mean: 107.76014870000097 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 154.17370893614557,
            "unit": "iter/sec",
            "range": "stddev: 0.0002228168453367471",
            "extra": "mean: 6.486190200004671 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 191.41235732537996,
            "unit": "iter/sec",
            "range": "stddev: 0.00010340693503883776",
            "extra": "mean: 5.224323099997719 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "florian.dobener@physik.uni-giessen.de",
            "name": "dobener",
            "username": "domna"
          },
          "committer": {
            "email": "florian.dobener@physik.uni-giessen.de",
            "name": "dobener",
            "username": "domna"
          },
          "distinct": true,
          "id": "1dfed78c29eeb39fe6f16248d6a1dc256089269d",
          "message": "Corrects typo and bugs in dispersions",
          "timestamp": "2021-12-09T11:52:29+01:00",
          "tree_id": "d007a16218e4b3babe9f9ab852bcaafe480b8bf0",
          "url": "https://github.com/PyEllips/pyElli/commit/1dfed78c29eeb39fe6f16248d6a1dc256089269d"
        },
        "date": 1639047411483,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 20.037481993592813,
            "unit": "iter/sec",
            "range": "stddev: 0.002731475253546686",
            "extra": "mean: 49.90647029999877 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_scipy",
            "value": 0.6997464821434117,
            "unit": "iter/sec",
            "range": "stddev: 0.04300080610323151",
            "extra": "mean: 1.4290889994000024 sec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 14.991569146284586,
            "unit": "iter/sec",
            "range": "stddev: 0.03882137539580026",
            "extra": "mean: 66.7041581999996 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 117.59716718776677,
            "unit": "iter/sec",
            "range": "stddev: 0.0003664804230844729",
            "extra": "mean: 8.503606199997193 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 136.2710240980444,
            "unit": "iter/sec",
            "range": "stddev: 0.00042532848731148987",
            "extra": "mean: 7.338317199997846 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "github@schroedingerscat.org",
            "name": "domna",
            "username": "domna"
          },
          "committer": {
            "email": "github@schroedingerscat.org",
            "name": "domna",
            "username": "domna"
          },
          "distinct": true,
          "id": "7349d0cbc78aad1af1bf815dba7f92255298a3f2",
          "message": "Corrects typo",
          "timestamp": "2021-12-12T23:20:20+01:00",
          "tree_id": "44d2b81581a9e9ef916cf54c8e8f2abf4521d8e9",
          "url": "https://github.com/PyEllips/pyElli/commit/7349d0cbc78aad1af1bf815dba7f92255298a3f2"
        },
        "date": 1639347754954,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 25.026588372618566,
            "unit": "iter/sec",
            "range": "stddev: 0.0006170571403498101",
            "extra": "mean: 39.957503800002314 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_scipy",
            "value": 1.0513403109360682,
            "unit": "iter/sec",
            "range": "stddev: 0.025581689545843826",
            "extra": "mean: 951.1668006999969 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 8.583278105660938,
            "unit": "iter/sec",
            "range": "stddev: 0.012287510125163532",
            "extra": "mean: 116.50560399999961 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 153.65792525177457,
            "unit": "iter/sec",
            "range": "stddev: 0.00015548851863240253",
            "extra": "mean: 6.507962399996359 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 177.51593782450956,
            "unit": "iter/sec",
            "range": "stddev: 0.00015969292735187995",
            "extra": "mean: 5.633297000005655 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "49639740+MarJMue@users.noreply.github.com",
            "name": "Marius Müller",
            "username": "MarJMue"
          },
          "committer": {
            "email": "49639740+MarJMue@users.noreply.github.com",
            "name": "Marius Müller",
            "username": "MarJMue"
          },
          "distinct": true,
          "id": "c984a16ecd1a1ce392adbb0166c1cd604e4f572b",
          "message": "Fix ResultList reinitialize error and include append and len method",
          "timestamp": "2021-12-17T10:51:24+01:00",
          "tree_id": "55ae4eb5a9740fd4ee8811c943dbcd0ea912fd78",
          "url": "https://github.com/PyEllips/pyElli/commit/c984a16ecd1a1ce392adbb0166c1cd604e4f572b"
        },
        "date": 1639734811609,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 26.202442740014902,
            "unit": "iter/sec",
            "range": "stddev: 0.0004941538569660768",
            "extra": "mean: 38.164380700004585 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_scipy",
            "value": 1.1365483567266899,
            "unit": "iter/sec",
            "range": "stddev: 0.020435614070165056",
            "extra": "mean: 879.8569757999957 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 8.57076745426111,
            "unit": "iter/sec",
            "range": "stddev: 0.008029711083541717",
            "extra": "mean: 116.67566590000433 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 152.09973069852242,
            "unit": "iter/sec",
            "range": "stddev: 0.00036121208097079314",
            "extra": "mean: 6.57463359999042 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 188.7402475555052,
            "unit": "iter/sec",
            "range": "stddev: 0.00011836682701944626",
            "extra": "mean: 5.298286999999391 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "49639740+MarJMue@users.noreply.github.com",
            "name": "Marius Müller",
            "username": "MarJMue"
          },
          "committer": {
            "email": "49639740+MarJMue@users.noreply.github.com",
            "name": "Marius Müller",
            "username": "MarJMue"
          },
          "distinct": true,
          "id": "224b2534e3829f51c87be849055125ad72a2b739",
          "message": "Update Examples to use ResultLists",
          "timestamp": "2021-12-17T10:51:46+01:00",
          "tree_id": "d1bfcb462ba6cc734cb028e085d2a70bbf593c2c",
          "url": "https://github.com/PyEllips/pyElli/commit/224b2534e3829f51c87be849055125ad72a2b739"
        },
        "date": 1639734901300,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 25.250051321357205,
            "unit": "iter/sec",
            "range": "stddev: 0.0004178755003808374",
            "extra": "mean: 39.60387990000527 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_scipy",
            "value": 1.0783378055582205,
            "unit": "iter/sec",
            "range": "stddev: 0.019964538356976345",
            "extra": "mean: 927.3531864000006 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 8.551017797677149,
            "unit": "iter/sec",
            "range": "stddev: 0.011191917676086141",
            "extra": "mean: 116.94514309999988 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 157.01384783633725,
            "unit": "iter/sec",
            "range": "stddev: 0.00029797780056913317",
            "extra": "mean: 6.368864999998891 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 190.3472220753162,
            "unit": "iter/sec",
            "range": "stddev: 0.0001388088912351707",
            "extra": "mean: 5.253557100004969 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "github@schroedingerscat.org",
            "name": "domna",
            "username": "domna"
          },
          "committer": {
            "email": "github@schroedingerscat.org",
            "name": "domna",
            "username": "domna"
          },
          "distinct": true,
          "id": "a2a5c93c25d30b77688aea6e97396dfab4f9dfaa",
          "message": "Adds a dispersion factory class (#30)",
          "timestamp": "2022-01-12T16:01:12+01:00",
          "tree_id": "7e2bc7dd2fb7d75bf38d205f9731bf300b23cf57",
          "url": "https://github.com/PyEllips/pyElli/commit/a2a5c93c25d30b77688aea6e97396dfab4f9dfaa"
        },
        "date": 1641999807105,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 24.960129001938917,
            "unit": "iter/sec",
            "range": "stddev: 0.0009157170910100102",
            "extra": "mean: 40.063895499991986 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_scipy",
            "value": 1.0419612615680596,
            "unit": "iter/sec",
            "range": "stddev: 0.026720049282882907",
            "extra": "mean: 959.7285781000039 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 9.10080008864914,
            "unit": "iter/sec",
            "range": "stddev: 0.014114984466074839",
            "extra": "mean: 109.8804489999992 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 158.042298440909,
            "unit": "iter/sec",
            "range": "stddev: 0.00031512521739302185",
            "extra": "mean: 6.327419999993822 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 194.2198200511452,
            "unit": "iter/sec",
            "range": "stddev: 0.00006672321329165732",
            "extra": "mean: 5.148805099997844 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "github@schroedingerscat.org",
            "name": "domna",
            "username": "domna"
          },
          "committer": {
            "email": "github@schroedingerscat.org",
            "name": "domna",
            "username": "domna"
          },
          "distinct": true,
          "id": "63ef321eb2fbc05a9f92eab048ef1a73aed60929",
          "message": "fixes typo in DispersionFactory",
          "timestamp": "2022-01-12T21:39:32+01:00",
          "tree_id": "e6978b1bbca2a273d8319438fcd1c6f0a98da512",
          "url": "https://github.com/PyEllips/pyElli/commit/63ef321eb2fbc05a9f92eab048ef1a73aed60929"
        },
        "date": 1642020101469,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 25.49446970138992,
            "unit": "iter/sec",
            "range": "stddev: 0.0004578940701245414",
            "extra": "mean: 39.22419300000115 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_scipy",
            "value": 1.0275714821331206,
            "unit": "iter/sec",
            "range": "stddev: 0.023934289591703416",
            "extra": "mean: 973.1683074000017 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 9.166090296798236,
            "unit": "iter/sec",
            "range": "stddev: 0.01468054414083724",
            "extra": "mean: 109.09776879999811 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 161.51028656583404,
            "unit": "iter/sec",
            "range": "stddev: 0.00015955104432718303",
            "extra": "mean: 6.191556100003481 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 194.03227730804372,
            "unit": "iter/sec",
            "range": "stddev: 0.00006487155657866316",
            "extra": "mean: 5.153781700002469 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "github@schroedingerscat.org",
            "name": "domna",
            "username": "domna"
          },
          "committer": {
            "email": "github@schroedingerscat.org",
            "name": "domna",
            "username": "domna"
          },
          "distinct": true,
          "id": "570acab275f30720f48fb33d037f0af87ffe034f",
          "message": "deletes print in test",
          "timestamp": "2022-01-12T21:40:11+01:00",
          "tree_id": "4e292dd0104a83e7a6aa1277852fd0066ef4bd5a",
          "url": "https://github.com/PyEllips/pyElli/commit/570acab275f30720f48fb33d037f0af87ffe034f"
        },
        "date": 1642020139709,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 25.467844170066357,
            "unit": "iter/sec",
            "range": "stddev: 0.0006816843106640542",
            "extra": "mean: 39.26520019999771 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_scipy",
            "value": 1.0308111609368535,
            "unit": "iter/sec",
            "range": "stddev: 0.023023749813981274",
            "extra": "mean: 970.1097911000005 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 8.865706123380127,
            "unit": "iter/sec",
            "range": "stddev: 0.01413240827451149",
            "extra": "mean: 112.79417410000292 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 162.46508665918608,
            "unit": "iter/sec",
            "range": "stddev: 0.00007713667682630155",
            "extra": "mean: 6.155168599994454 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 193.56071878771442,
            "unit": "iter/sec",
            "range": "stddev: 0.000059697343139182434",
            "extra": "mean: 5.166337500000395 msec\nrounds: 10"
          }
        ]
      }
    ]
  }
}