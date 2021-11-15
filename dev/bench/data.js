window.BENCHMARK_DATA = {
  "lastUpdate": 1636976929555,
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
      }
    ]
  }
}