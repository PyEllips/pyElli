window.BENCHMARK_DATA = {
  "lastUpdate": 1679503052555,
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
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
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
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
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
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
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
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
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
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
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
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
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
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
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
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
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
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
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
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
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
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
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
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
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
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
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
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
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
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
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
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
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
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
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
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
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
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
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
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
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
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
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
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
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
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
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
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
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
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
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
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
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
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
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
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
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
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
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
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
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
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
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
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
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
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
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
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
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
          "id": "6443d68da4935459e10f6f0a13e3d12d89f1837b",
          "message": "fixes typo in solver2x2",
          "timestamp": "2022-01-24T13:37:08+01:00",
          "tree_id": "9c45213cd1b7a1796df29df308050f838e08598e",
          "url": "https://github.com/PyEllips/pyElli/commit/6443d68da4935459e10f6f0a13e3d12d89f1837b"
        },
        "date": 1643027999297,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 18.24622676514976,
            "unit": "iter/sec",
            "range": "stddev: 0.0018569387747947828",
            "extra": "mean: 54.80585180000048 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 0.5854712175835194,
            "unit": "iter/sec",
            "range": "stddev: 0.0236855469493771",
            "extra": "mean: 1.708025894299999 sec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 10.82249379230948,
            "unit": "iter/sec",
            "range": "stddev: 0.04271291841476698",
            "extra": "mean: 92.40014540000061 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 102.13995461715895,
            "unit": "iter/sec",
            "range": "stddev: 0.0016216453031752801",
            "extra": "mean: 9.790488000001574 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 128.47531838823215,
            "unit": "iter/sec",
            "range": "stddev: 0.0002851990097023767",
            "extra": "mean: 7.783596199996623 msec\nrounds: 10"
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
          "id": "b276f46bf3059d92bafce42d4b9f26d9036188a4",
          "message": "adds test for TiO2 (fixes #42)",
          "timestamp": "2022-01-26T12:58:33+01:00",
          "tree_id": "7fdaebb05acfe0bb26637f0dfa1f65a640ac7889",
          "url": "https://github.com/PyEllips/pyElli/commit/b276f46bf3059d92bafce42d4b9f26d9036188a4"
        },
        "date": 1643198446115,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 24.908910170491716,
            "unit": "iter/sec",
            "range": "stddev: 0.0022140128701067553",
            "extra": "mean: 40.14627669999982 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 1.0475954617056218,
            "unit": "iter/sec",
            "range": "stddev: 0.017197415416475428",
            "extra": "mean: 954.5669455000024 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 9.50514765101,
            "unit": "iter/sec",
            "range": "stddev: 0.011380660383730068",
            "extra": "mean: 105.20615110000335 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 156.85091054304846,
            "unit": "iter/sec",
            "range": "stddev: 0.00024236040425194507",
            "extra": "mean: 6.375481000000605 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 189.5276389386913,
            "unit": "iter/sec",
            "range": "stddev: 0.00017244438152350284",
            "extra": "mean: 5.276275300002453 msec\nrounds: 10"
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
          "id": "69735432f6b5e441134ec4ba49a117cfc700b5fa",
          "message": "fixes directory slash in TiO2 test",
          "timestamp": "2022-01-26T13:02:59+01:00",
          "tree_id": "338c5e7fd6bb44892d16ed68cc54baba72815be8",
          "url": "https://github.com/PyEllips/pyElli/commit/69735432f6b5e441134ec4ba49a117cfc700b5fa"
        },
        "date": 1643198702726,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 24.477130252294682,
            "unit": "iter/sec",
            "range": "stddev: 0.0032301421179962773",
            "extra": "mean: 40.854462500000466 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 1.0386267092857344,
            "unit": "iter/sec",
            "range": "stddev: 0.031132162723481377",
            "extra": "mean: 962.8098248000015 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 8.683503559787793,
            "unit": "iter/sec",
            "range": "stddev: 0.009774933784061348",
            "extra": "mean: 115.1608901999964 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 154.51016961969813,
            "unit": "iter/sec",
            "range": "stddev: 0.0002593475308218689",
            "extra": "mean: 6.472065900007351 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 169.34813921549295,
            "unit": "iter/sec",
            "range": "stddev: 0.0012537432487010336",
            "extra": "mean: 5.904995499994925 msec\nrounds: 10"
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
          "id": "2429ca8f41ffcdeffdf4340e2cd67c658146d45c",
          "message": "fixes directory in TiO2 for real",
          "timestamp": "2022-01-26T13:09:17+01:00",
          "tree_id": "d3ffcd06b3c02054ff2320571455f2679ee50c5c",
          "url": "https://github.com/PyEllips/pyElli/commit/2429ca8f41ffcdeffdf4340e2cd67c658146d45c"
        },
        "date": 1643199093047,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 26.52441931806399,
            "unit": "iter/sec",
            "range": "stddev: 0.0008838767221603862",
            "extra": "mean: 37.70110809999778 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 1.1181859260197706,
            "unit": "iter/sec",
            "range": "stddev: 0.021631599450788325",
            "extra": "mean: 894.305657700005 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 9.132336165571692,
            "unit": "iter/sec",
            "range": "stddev: 0.012281685149525302",
            "extra": "mean: 109.50100630000179 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 153.49026894715655,
            "unit": "iter/sec",
            "range": "stddev: 0.0002606062657654581",
            "extra": "mean: 6.515071000001171 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 189.82820016370977,
            "unit": "iter/sec",
            "range": "stddev: 0.00017880541562937763",
            "extra": "mean: 5.267921199998682 msec\nrounds: 10"
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
          "id": "318ca4e62e04089c379cd2e4bfda67b48a6b4786",
          "message": "allows for inf values in boundedfloat (fixes #43)",
          "timestamp": "2022-01-26T15:34:27+01:00",
          "tree_id": "2a48435fad8309f6bc743e463e909c8d8d50349c",
          "url": "https://github.com/PyEllips/pyElli/commit/318ca4e62e04089c379cd2e4bfda67b48a6b4786"
        },
        "date": 1643207800114,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 24.702103500705867,
            "unit": "iter/sec",
            "range": "stddev: 0.0004926797065298932",
            "extra": "mean: 40.48238240000188 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 1.0888747727792485,
            "unit": "iter/sec",
            "range": "stddev: 0.016142393574982823",
            "extra": "mean: 918.3792525999991 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 9.821721011417857,
            "unit": "iter/sec",
            "range": "stddev: 0.032644665726367254",
            "extra": "mean: 101.8151501999995 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 161.61606497303808,
            "unit": "iter/sec",
            "range": "stddev: 0.00010056324884670697",
            "extra": "mean: 6.187503699999297 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 188.51399320513528,
            "unit": "iter/sec",
            "range": "stddev: 0.00010677176448360871",
            "extra": "mean: 5.304646000001867 msec\nrounds: 10"
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
          "id": "a9dcc6b283d9a22ecf1760c99b93013a15a12f3b",
          "message": "cleans TiO2 tests",
          "timestamp": "2022-01-26T21:52:58+01:00",
          "tree_id": "f3f37ad0a8615db9948ca93202bcc53d7d4ea6bb",
          "url": "https://github.com/PyEllips/pyElli/commit/a9dcc6b283d9a22ecf1760c99b93013a15a12f3b"
        },
        "date": 1643230498370,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 27.218831956414206,
            "unit": "iter/sec",
            "range": "stddev: 0.000750480977527187",
            "extra": "mean: 36.739269399998875 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 1.1189998367821226,
            "unit": "iter/sec",
            "range": "stddev: 0.027617870143706355",
            "extra": "mean: 893.6551795000014 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 9.933887820897962,
            "unit": "iter/sec",
            "range": "stddev: 0.01279867776142443",
            "extra": "mean: 100.66552170000307 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 167.08049441993438,
            "unit": "iter/sec",
            "range": "stddev: 0.00019225439289893162",
            "extra": "mean: 5.985139099999515 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 193.21394746578048,
            "unit": "iter/sec",
            "range": "stddev: 0.0008111349269723393",
            "extra": "mean: 5.175609799997005 msec\nrounds: 10"
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
          "id": "8449738662d7d2a5084557eca673e9f436e4d6c2",
          "message": "Include Looyenga Mixture",
          "timestamp": "2022-02-25T15:41:40+01:00",
          "tree_id": "a909f2ef72ba306d2a9701d19dadf2fca3f5cd1d",
          "url": "https://github.com/PyEllips/pyElli/commit/8449738662d7d2a5084557eca673e9f436e4d6c2"
        },
        "date": 1645800233092,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 24.498855455119315,
            "unit": "iter/sec",
            "range": "stddev: 0.00031754462967516277",
            "extra": "mean: 40.81823340000312 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 1.091076967383712,
            "unit": "iter/sec",
            "range": "stddev: 0.015927466622842095",
            "extra": "mean: 916.5256255000003 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 9.886164913776161,
            "unit": "iter/sec",
            "range": "stddev: 0.032158377000660494",
            "extra": "mean: 101.15145850000147 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 151.05190963809505,
            "unit": "iter/sec",
            "range": "stddev: 0.0014160903444367684",
            "extra": "mean: 6.620240700007685 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 189.5491399319652,
            "unit": "iter/sec",
            "range": "stddev: 0.00008015828740608183",
            "extra": "mean: 5.275676800005158 msec\nrounds: 10"
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
            "email": "florian.dobener@physik.uni-giessen.de",
            "name": "Florian Dobener",
            "username": "domna"
          },
          "distinct": true,
          "id": "ca7fa21782c70fd9591b902a57294b5fae27892c",
          "message": "Fixes benchmark",
          "timestamp": "2022-03-16T14:05:08+01:00",
          "tree_id": "a9ae5270ac0bc6e1bb4875aee7e02162797c214c",
          "url": "https://github.com/PyEllips/pyElli/commit/ca7fa21782c70fd9591b902a57294b5fae27892c"
        },
        "date": 1647436040048,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 24.449754366030533,
            "unit": "iter/sec",
            "range": "stddev: 0.0007459167934692585",
            "extra": "mean: 40.90020640000205 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 1.079638574464412,
            "unit": "iter/sec",
            "range": "stddev: 0.0169774590583994",
            "extra": "mean: 926.2358937999977 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 8.528410765569074,
            "unit": "iter/sec",
            "range": "stddev: 0.007263286028013063",
            "extra": "mean: 117.25514020000105 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 159.5522835282327,
            "unit": "iter/sec",
            "range": "stddev: 0.00012563575261092177",
            "extra": "mean: 6.267538000000172 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 192.91218263211402,
            "unit": "iter/sec",
            "range": "stddev: 0.0000812315999109991",
            "extra": "mean: 5.183705799996119 msec\nrounds: 10"
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
            "email": "florian.dobener@physik.uni-giessen.de",
            "name": "Florian Dobener",
            "username": "domna"
          },
          "distinct": true,
          "id": "0ba0f39f43ee5e935f58faacbde9a37fda9bc6ac",
          "message": "Updates: CHANGELOG",
          "timestamp": "2022-03-16T14:14:05+01:00",
          "tree_id": "f2693e69cce51234a3dd803880c94476cba4c8da",
          "url": "https://github.com/PyEllips/pyElli/commit/0ba0f39f43ee5e935f58faacbde9a37fda9bc6ac"
        },
        "date": 1647436598479,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 20.933051018204775,
            "unit": "iter/sec",
            "range": "stddev: 0.003731168066600147",
            "extra": "mean: 47.77134490000208 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 0.9140845933610643,
            "unit": "iter/sec",
            "range": "stddev: 0.0372756649667864",
            "extra": "mean: 1.0939906516999998 sec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 7.299795098766173,
            "unit": "iter/sec",
            "range": "stddev: 0.025096681399564218",
            "extra": "mean: 136.9901465000055 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 116.58519809613531,
            "unit": "iter/sec",
            "range": "stddev: 0.002098433215158655",
            "extra": "mean: 8.5774181999966 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 129.97890871238576,
            "unit": "iter/sec",
            "range": "stddev: 0.0025141145360485454",
            "extra": "mean: 7.693555900002025 msec\nrounds: 10"
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
          "id": "608430634348ff5750cddb9f01a5a52f0e2883fc",
          "message": "Fix Benchmark",
          "timestamp": "2022-04-30T13:19:58+02:00",
          "tree_id": "2220e79defe812c4f861f849e65a321f5a804f82",
          "url": "https://github.com/PyEllips/pyElli/commit/608430634348ff5750cddb9f01a5a52f0e2883fc"
        },
        "date": 1651317796052,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 24.44552901651262,
            "unit": "iter/sec",
            "range": "stddev: 0.0007842255146472309",
            "extra": "mean: 40.90727590000256 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 1.028325708263068,
            "unit": "iter/sec",
            "range": "stddev: 0.024025878894922983",
            "extra": "mean: 972.454536500004 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 9.68895431749287,
            "unit": "iter/sec",
            "range": "stddev: 0.029901063247939574",
            "extra": "mean: 103.21031220000236 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 146.4765362166549,
            "unit": "iter/sec",
            "range": "stddev: 0.0008916317844047623",
            "extra": "mean: 6.827031999998212 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 180.15971663315898,
            "unit": "iter/sec",
            "range": "stddev: 0.00029995646708535166",
            "extra": "mean: 5.550630400003342 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "committer": {
            "email": "49639740+MarJMue@users.noreply.github.com",
            "name": "Marius Müller",
            "username": "MarJMue"
          },
          "distinct": true,
          "id": "b7368957444e1f7b40c06558552e7faa77e294ff",
          "message": "Sets plotly as backend in psi_delta decorator",
          "timestamp": "2022-06-21T08:56:02+02:00",
          "tree_id": "be31c222e4c148a324563664cd811f35a85491d4",
          "url": "https://github.com/PyEllips/pyElli/commit/b7368957444e1f7b40c06558552e7faa77e294ff"
        },
        "date": 1655794697726,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 24.56158685024401,
            "unit": "iter/sec",
            "range": "stddev: 0.002183100902430757",
            "extra": "mean: 40.713981800001875 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 1.0532565797387494,
            "unit": "iter/sec",
            "range": "stddev: 0.030181544812201703",
            "extra": "mean: 949.4362714999994 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 8.29030009884887,
            "unit": "iter/sec",
            "range": "stddev: 0.0069467541466228504",
            "extra": "mean: 120.62289520000036 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 156.72656385032542,
            "unit": "iter/sec",
            "range": "stddev: 0.0003255204114938501",
            "extra": "mean: 6.38053929999387 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 191.7652032986272,
            "unit": "iter/sec",
            "range": "stddev: 0.000057586746971937294",
            "extra": "mean: 5.214710400002787 msec\nrounds: 10"
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
          "id": "a7484ddaa393534608375e9e405d9d8ca884323e",
          "message": "Improve Testing (#48)\n\n* Test with all current python versions\r\n\r\n* Test python 3.10 not 3.1\r\n\r\n* Include basic test for fitting decorator\r\n\r\n* Simplifies test to use matrix\r\n\r\n* Corrects action to call matrix correctly\r\n\r\nCo-authored-by: domna <florian.dobener@physik.hu-berlin.de>",
          "timestamp": "2022-06-21T10:54:16+02:00",
          "tree_id": "9bcb01684736f7d314004e111ad0357bb278656d",
          "url": "https://github.com/PyEllips/pyElli/commit/a7484ddaa393534608375e9e405d9d8ca884323e"
        },
        "date": 1655802411351,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 26.810806136166836,
            "unit": "iter/sec",
            "range": "stddev: 0.0008701624475220496",
            "extra": "mean: 37.29839359999829 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 1.1186921333218258,
            "unit": "iter/sec",
            "range": "stddev: 0.0370307717935509",
            "extra": "mean: 893.9009850999995 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 9.46434102203469,
            "unit": "iter/sec",
            "range": "stddev: 0.02428365196690816",
            "extra": "mean: 105.65975990000993 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 158.68017699314936,
            "unit": "iter/sec",
            "range": "stddev: 0.0001685420993623216",
            "extra": "mean: 6.301984399999583 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 189.9639824488798,
            "unit": "iter/sec",
            "range": "stddev: 0.00044090405285718303",
            "extra": "mean: 5.264155800003323 msec\nrounds: 10"
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
          "id": "45e2e2dc4bd609f16a53fbcb9a263e7b6d67198d",
          "message": "Merge pull request #56 from PyEllips/nexus-reader\n\nImplement Nexus file format reader",
          "timestamp": "2022-06-29T15:29:34+02:00",
          "tree_id": "dfc2f5651f637038ce56134a305bbca293279766",
          "url": "https://github.com/PyEllips/pyElli/commit/45e2e2dc4bd609f16a53fbcb9a263e7b6d67198d"
        },
        "date": 1656509506476,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 20.885069653836815,
            "unit": "iter/sec",
            "range": "stddev: 0.002412817495566617",
            "extra": "mean: 47.88109480000173 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 0.7137952108380548,
            "unit": "iter/sec",
            "range": "stddev: 0.046493594760440585",
            "extra": "mean: 1.400962047400006 sec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 15.7513716798505,
            "unit": "iter/sec",
            "range": "stddev: 0.032537250004056516",
            "extra": "mean: 63.48653439999907 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 107.77483801548833,
            "unit": "iter/sec",
            "range": "stddev: 0.0012171782044414173",
            "extra": "mean: 9.278603600000679 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 145.3861832851166,
            "unit": "iter/sec",
            "range": "stddev: 0.00017568838891354957",
            "extra": "mean: 6.878232700000808 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "Florian Dobener",
            "username": "domna"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "5c05a3edf2c0d3647f7e0edb18a70678f7a55be6",
          "message": "Update CHANGELOG.md",
          "timestamp": "2022-06-29T15:38:34+02:00",
          "tree_id": "138a44fe3cb48f1c2a16da0a85e18d96d11a3f30",
          "url": "https://github.com/PyEllips/pyElli/commit/5c05a3edf2c0d3647f7e0edb18a70678f7a55be6"
        },
        "date": 1656510037172,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 23.609021440561552,
            "unit": "iter/sec",
            "range": "stddev: 0.002186826410547973",
            "extra": "mean: 42.35668989998658 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 1.1067296464039504,
            "unit": "iter/sec",
            "range": "stddev: 0.022585751894937993",
            "extra": "mean: 903.5630366000021 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 9.261057876748438,
            "unit": "iter/sec",
            "range": "stddev: 0.026496556742276942",
            "extra": "mean: 107.97902500001442 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 154.0191125705344,
            "unit": "iter/sec",
            "range": "stddev: 0.00018558331273164515",
            "extra": "mean: 6.492700699999432 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 186.8157650759789,
            "unit": "iter/sec",
            "range": "stddev: 0.0001151812732770334",
            "extra": "mean: 5.352867300001662 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "committer": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "distinct": true,
          "id": "29d42397cebab8977bd6c9e094cf7a01e8cc6bc7",
          "message": "Updates dockerfile",
          "timestamp": "2022-07-07T22:52:26+02:00",
          "tree_id": "3b43b44f6d7a96447c17684cc7c8dc63af6444d3",
          "url": "https://github.com/PyEllips/pyElli/commit/29d42397cebab8977bd6c9e094cf7a01e8cc6bc7"
        },
        "date": 1657227295449,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 18.096058951431058,
            "unit": "iter/sec",
            "range": "stddev: 0.0015448943075683412",
            "extra": "mean: 55.260651099996494 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 0.6310457179614261,
            "unit": "iter/sec",
            "range": "stddev: 0.03372174839824892",
            "extra": "mean: 1.5846712394000064 sec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 11.202662932129194,
            "unit": "iter/sec",
            "range": "stddev: 0.04287850459728752",
            "extra": "mean: 89.26449059999868 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 106.00544484243557,
            "unit": "iter/sec",
            "range": "stddev: 0.00023558534836822577",
            "extra": "mean: 9.433477700002868 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 125.78636762802064,
            "unit": "iter/sec",
            "range": "stddev: 0.0002789039024784309",
            "extra": "mean: 7.949987100010958 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "committer": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "distinct": true,
          "id": "2a48c0fa107f8ee2ab7b13c1318961664825f2c8",
          "message": "Updates dockerfile",
          "timestamp": "2022-07-07T22:53:44+02:00",
          "tree_id": "4dc8eac67b02f252f25d5d830716abad42029a80",
          "url": "https://github.com/PyEllips/pyElli/commit/2a48c0fa107f8ee2ab7b13c1318961664825f2c8"
        },
        "date": 1657227346493,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 25.02499440134519,
            "unit": "iter/sec",
            "range": "stddev: 0.0006141533147929942",
            "extra": "mean: 39.9600489000008 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 1.1072501090660736,
            "unit": "iter/sec",
            "range": "stddev: 0.014657185679842935",
            "extra": "mean: 903.1383169999998 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 8.914150124459056,
            "unit": "iter/sec",
            "range": "stddev: 0.011823638614408358",
            "extra": "mean: 112.18119350000109 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 162.58139190295324,
            "unit": "iter/sec",
            "range": "stddev: 0.00011037808926294848",
            "extra": "mean: 6.1507653999967715 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 187.52488455221106,
            "unit": "iter/sec",
            "range": "stddev: 0.0006084733685660749",
            "extra": "mean: 5.332625599999119 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "committer": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "distinct": true,
          "id": "f4d8c721cc0b0da4cd71ad0a88a8b6afd0bc8204",
          "message": "Updates dockerfile",
          "timestamp": "2022-07-07T22:55:58+02:00",
          "tree_id": "61e1d9199569592a49beb9d051bc4c5f6e477bc2",
          "url": "https://github.com/PyEllips/pyElli/commit/f4d8c721cc0b0da4cd71ad0a88a8b6afd0bc8204"
        },
        "date": 1657227482615,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 25.229916698692993,
            "unit": "iter/sec",
            "range": "stddev: 0.0007305219477464572",
            "extra": "mean: 39.63548559999026 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 1.072450761517039,
            "unit": "iter/sec",
            "range": "stddev: 0.030873200761528833",
            "extra": "mean: 932.4437408999984 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 8.947496157862322,
            "unit": "iter/sec",
            "range": "stddev: 0.01154442865919354",
            "extra": "mean: 111.76311030000079 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 158.75384833222247,
            "unit": "iter/sec",
            "range": "stddev: 0.0002144413722134404",
            "extra": "mean: 6.299059899998838 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 191.57663586518836,
            "unit": "iter/sec",
            "range": "stddev: 0.00009707880119929447",
            "extra": "mean: 5.219843200001151 msec\nrounds: 10"
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
          "id": "a68c6c51b2cd2863fe363fbd57bd4e8c2d5febf7",
          "message": "Merge pull request #68 from PyEllips/docs\n\nComplete overhaul of the documentation structure and content.",
          "timestamp": "2022-07-18T20:55:46+02:00",
          "tree_id": "b03032730b0915dd4152a5471d1a8e53bf866dec",
          "url": "https://github.com/PyEllips/pyElli/commit/a68c6c51b2cd2863fe363fbd57bd4e8c2d5febf7"
        },
        "date": 1658170663960,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 24.497814463004996,
            "unit": "iter/sec",
            "range": "stddev: 0.001465436470605472",
            "extra": "mean: 40.8199678999992 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 1.0724145913045884,
            "unit": "iter/sec",
            "range": "stddev: 0.02806895651315839",
            "extra": "mean: 932.4751901999988 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 8.544000401636577,
            "unit": "iter/sec",
            "range": "stddev: 0.01055310062095143",
            "extra": "mean: 117.04119299999718 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 141.60010211066208,
            "unit": "iter/sec",
            "range": "stddev: 0.00023762539088053068",
            "extra": "mean: 7.062141800000177 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 164.14479258121503,
            "unit": "iter/sec",
            "range": "stddev: 0.000041373510415117966",
            "extra": "mean: 6.092182299997262 msec\nrounds: 10"
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
          "id": "269b39831f25dbc1117ec140df27296f70166d70",
          "message": "Update docs requirements.txt",
          "timestamp": "2022-07-18T21:02:35+02:00",
          "tree_id": "3b8df6ae9d023730f99d3a37966487807a2690e1",
          "url": "https://github.com/PyEllips/pyElli/commit/269b39831f25dbc1117ec140df27296f70166d70"
        },
        "date": 1658171107602,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 19.354058266643488,
            "unit": "iter/sec",
            "range": "stddev: 0.0007696852034251012",
            "extra": "mean: 51.66875009999785 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 0.6388597469732281,
            "unit": "iter/sec",
            "range": "stddev: 0.055578933411835514",
            "extra": "mean: 1.5652887894999992 sec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 11.011032509528158,
            "unit": "iter/sec",
            "range": "stddev: 0.03545236135509049",
            "extra": "mean: 90.8180045000023 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 109.94352311163563,
            "unit": "iter/sec",
            "range": "stddev: 0.0005041272046291966",
            "extra": "mean: 9.09557899999811 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 127.01524289599222,
            "unit": "iter/sec",
            "range": "stddev: 0.00019175340644676507",
            "extra": "mean: 7.8730708000051655 msec\nrounds: 10"
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
          "id": "bf01588a15f3a32f5c1eff9dc02947796f622084",
          "message": "Also include h5py in docs requirements",
          "timestamp": "2022-07-18T21:05:42+02:00",
          "tree_id": "fe35a5af8411a19b4941c27c554b349cafb4b95d",
          "url": "https://github.com/PyEllips/pyElli/commit/bf01588a15f3a32f5c1eff9dc02947796f622084"
        },
        "date": 1658171274952,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 21.207342176120097,
            "unit": "iter/sec",
            "range": "stddev: 0.0013326295545154326",
            "extra": "mean: 47.15348070000118 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 0.941727837745702,
            "unit": "iter/sec",
            "range": "stddev: 0.03978545187382683",
            "extra": "mean: 1.0618779226000044 sec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 7.661100711264661,
            "unit": "iter/sec",
            "range": "stddev: 0.013982629843166923",
            "extra": "mean: 130.52954630000215 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 138.51957837795578,
            "unit": "iter/sec",
            "range": "stddev: 0.000170966746988575",
            "extra": "mean: 7.219196100001568 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 164.4718176718619,
            "unit": "iter/sec",
            "range": "stddev: 0.00020445956364840366",
            "extra": "mean: 6.080068999997934 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "committer": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "distinct": true,
          "id": "4d49cf33dc43a8a26ddb019cb40dbf8bd8b0386f",
          "message": "Updates README and CONTRIBUTING",
          "timestamp": "2022-07-20T21:31:29+02:00",
          "tree_id": "8615ba4f5b6050eb871a048f9f6936d4397046e8",
          "url": "https://github.com/PyEllips/pyElli/commit/4d49cf33dc43a8a26ddb019cb40dbf8bd8b0386f"
        },
        "date": 1658345612148,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 25.844841774311227,
            "unit": "iter/sec",
            "range": "stddev: 0.0012159068868355723",
            "extra": "mean: 38.69244040000126 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 1.1116425384964852,
            "unit": "iter/sec",
            "range": "stddev: 0.039036778026644764",
            "extra": "mean: 899.5697496000076 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 10.995124290199472,
            "unit": "iter/sec",
            "range": "stddev: 0.030123626000847233",
            "extra": "mean: 90.94940389999522 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 157.59787304657522,
            "unit": "iter/sec",
            "range": "stddev: 0.00011009069328947582",
            "extra": "mean: 6.345263299996873 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 194.09850860351733,
            "unit": "iter/sec",
            "range": "stddev: 0.000056199381017686425",
            "extra": "mean: 5.152023099995517 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "committer": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "distinct": true,
          "id": "1444549f51594ac7fd478e10381de35e3a90a55c",
          "message": "Updates link in changelog",
          "timestamp": "2022-07-21T19:05:25+02:00",
          "tree_id": "80d3d1d796a42d5ac4cd589f19bbbbdbafaebd8a",
          "url": "https://github.com/PyEllips/pyElli/commit/1444549f51594ac7fd478e10381de35e3a90a55c"
        },
        "date": 1658423270439,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 20.213301551880743,
            "unit": "iter/sec",
            "range": "stddev: 0.0006005352243256821",
            "extra": "mean: 49.47237329999439 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 0.8903866549770614,
            "unit": "iter/sec",
            "range": "stddev: 0.038822894745069586",
            "extra": "mean: 1.1231075784999973 sec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 7.254294348202528,
            "unit": "iter/sec",
            "range": "stddev: 0.0160428557597785",
            "extra": "mean: 137.84938299998544 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 129.4310325708735,
            "unit": "iter/sec",
            "range": "stddev: 0.0002913025076638366",
            "extra": "mean: 7.726122399992619 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 153.4262851139898,
            "unit": "iter/sec",
            "range": "stddev: 0.00046493730610141587",
            "extra": "mean: 6.517787999996472 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "committer": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "distinct": true,
          "id": "c1aa6cb050e55498895ed2dff4f578d715ed87b4",
          "message": "Disables display of sphinx-gallery config comments",
          "timestamp": "2022-07-22T21:31:02+02:00",
          "tree_id": "f0e2904bcae7315324a869bb88ea2a6e21cdd1c0",
          "url": "https://github.com/PyEllips/pyElli/commit/c1aa6cb050e55498895ed2dff4f578d715ed87b4"
        },
        "date": 1658518406963,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 19.322839289962378,
            "unit": "iter/sec",
            "range": "stddev: 0.004835121971196587",
            "extra": "mean: 51.75222880001229 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 0.9081318758455182,
            "unit": "iter/sec",
            "range": "stddev: 0.025550671023944493",
            "extra": "mean: 1.1011616557000026 sec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 11.57944497983152,
            "unit": "iter/sec",
            "range": "stddev: 0.04119831540501638",
            "extra": "mean: 86.35992500001066 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 117.77854818040117,
            "unit": "iter/sec",
            "range": "stddev: 0.00018816958531396583",
            "extra": "mean: 8.490510499996162 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 136.32238892676264,
            "unit": "iter/sec",
            "range": "stddev: 0.0012919411963209352",
            "extra": "mean: 7.33555219999289 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "committer": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "distinct": true,
          "id": "dffd6ed54a985001ff8c9ed0de3b9e42575b6aa0",
          "message": "Disables display of sphinx-gallery config comments",
          "timestamp": "2022-07-22T21:31:58+02:00",
          "tree_id": "f0e2904bcae7315324a869bb88ea2a6e21cdd1c0",
          "url": "https://github.com/PyEllips/pyElli/commit/dffd6ed54a985001ff8c9ed0de3b9e42575b6aa0"
        },
        "date": 1658518468715,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 19.3827878018296,
            "unit": "iter/sec",
            "range": "stddev: 0.005460461850525514",
            "extra": "mean: 51.592165700003534 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 0.888344129736656,
            "unit": "iter/sec",
            "range": "stddev: 0.06216398390072727",
            "extra": "mean: 1.1256898836000004 sec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 11.123958504510203,
            "unit": "iter/sec",
            "range": "stddev: 0.05162364219705673",
            "extra": "mean: 89.89605629997186 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 128.17591724257863,
            "unit": "iter/sec",
            "range": "stddev: 0.0001913208690318993",
            "extra": "mean: 7.801777599979687 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 142.42892419219115,
            "unit": "iter/sec",
            "range": "stddev: 0.0013414481100803351",
            "extra": "mean: 7.021045800013326 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "committer": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "distinct": true,
          "id": "c5d0cf2adc87d636e3005f383d914da88dc97f21",
          "message": "Disables display of sphinx-gallery config comments",
          "timestamp": "2022-07-22T21:34:24+02:00",
          "tree_id": "dce7cce03c3e31a3e8744ddb432ea838a519e5f4",
          "url": "https://github.com/PyEllips/pyElli/commit/c5d0cf2adc87d636e3005f383d914da88dc97f21"
        },
        "date": 1658518598398,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 21.532196755751126,
            "unit": "iter/sec",
            "range": "stddev: 0.004073106717432048",
            "extra": "mean: 46.442079800004876 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 1.0743280371526522,
            "unit": "iter/sec",
            "range": "stddev: 0.017129040557651014",
            "extra": "mean: 930.8143932000064 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 8.909794117021674,
            "unit": "iter/sec",
            "range": "stddev: 0.03382942174592563",
            "extra": "mean: 112.2360389999983 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 133.83995682962862,
            "unit": "iter/sec",
            "range": "stddev: 0.0017803316751019624",
            "extra": "mean: 7.47161030000143 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 39.4432792549084,
            "unit": "iter/sec",
            "range": "stddev: 0.0626671546464141",
            "extra": "mean: 25.352861600003962 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "committer": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "distinct": true,
          "id": "da66dc3d00d0d4cf433c1f32d5def0b5a47a530b",
          "message": "Disables display of sphinx-gallery config comments",
          "timestamp": "2022-07-22T21:36:37+02:00",
          "tree_id": "4270cd345aff651e697a4cb18a2901d47063a41d",
          "url": "https://github.com/PyEllips/pyElli/commit/da66dc3d00d0d4cf433c1f32d5def0b5a47a530b"
        },
        "date": 1658518718609,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 22.934471552194275,
            "unit": "iter/sec",
            "range": "stddev: 0.00424184428246943",
            "extra": "mean: 43.60248710000576 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 1.0553721278517285,
            "unit": "iter/sec",
            "range": "stddev: 0.028194225707524525",
            "extra": "mean: 947.5330773000024 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 14.866371368696088,
            "unit": "iter/sec",
            "range": "stddev: 0.040443540594739036",
            "extra": "mean: 67.26591010000504 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 154.57415770207368,
            "unit": "iter/sec",
            "range": "stddev: 0.00014767074539866507",
            "extra": "mean: 6.469386699990309 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 173.66184690201007,
            "unit": "iter/sec",
            "range": "stddev: 0.001263363621484068",
            "extra": "mean: 5.758317200002239 msec\nrounds: 10"
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
          "id": "4b32bbe0c80ad4d83ec4358832ef000e2956b70d",
          "message": "Merge pull request #71 from PyEllips/BruggemanEMA\n\nAdd a Bruggeman EMA material",
          "timestamp": "2022-07-25T09:52:26+02:00",
          "tree_id": "429e3f30988b5c7b095292af2799e36c593210df",
          "url": "https://github.com/PyEllips/pyElli/commit/4b32bbe0c80ad4d83ec4358832ef000e2956b70d"
        },
        "date": 1658735676280,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 25.360440651854812,
            "unit": "iter/sec",
            "range": "stddev: 0.00384294236414446",
            "extra": "mean: 39.43149150000522 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 1.1796981299003915,
            "unit": "iter/sec",
            "range": "stddev: 0.021312834353681837",
            "extra": "mean: 847.6744810000127 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 11.326305414434263,
            "unit": "iter/sec",
            "range": "stddev: 0.04646017251321293",
            "extra": "mean: 88.29004370000462 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 152.2095545648825,
            "unit": "iter/sec",
            "range": "stddev: 0.0005463340633884651",
            "extra": "mean: 6.569889800010742 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 168.6717635000637,
            "unit": "iter/sec",
            "range": "stddev: 0.0013981584551880633",
            "extra": "mean: 5.928674599999795 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "committer": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "distinct": true,
          "id": "2d03e1f5594d66fbeda953002bb93e0029eb24f7",
          "message": "Fixes docs",
          "timestamp": "2022-07-25T12:18:31+02:00",
          "tree_id": "76d61cead09bb5b3f767d71bd21b3d3f1bed2eb2",
          "url": "https://github.com/PyEllips/pyElli/commit/2d03e1f5594d66fbeda953002bb93e0029eb24f7"
        },
        "date": 1658744439121,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 23.405272621850365,
            "unit": "iter/sec",
            "range": "stddev: 0.003365344279545273",
            "extra": "mean: 42.725415600006045 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 1.039704877533069,
            "unit": "iter/sec",
            "range": "stddev: 0.01766613583981537",
            "extra": "mean: 961.8113962999985 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 14.180075257202779,
            "unit": "iter/sec",
            "range": "stddev: 0.03588829493406293",
            "extra": "mean: 70.5214875000081 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 156.59560405111313,
            "unit": "iter/sec",
            "range": "stddev: 0.00017072685419345523",
            "extra": "mean: 6.385875300009047 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 168.75798309635002,
            "unit": "iter/sec",
            "range": "stddev: 0.0013603522320856456",
            "extra": "mean: 5.925645600001417 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "committer": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "distinct": true,
          "id": "b8721496f2186405e25522e7ae899356481bc201",
          "message": "Removes overview from docs index",
          "timestamp": "2022-07-25T13:06:38+02:00",
          "tree_id": "c6dd22b067cc950073d4570812eb6b7d40ed9afb",
          "url": "https://github.com/PyEllips/pyElli/commit/b8721496f2186405e25522e7ae899356481bc201"
        },
        "date": 1658747328751,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 23.133574210594674,
            "unit": "iter/sec",
            "range": "stddev: 0.005760555758118388",
            "extra": "mean: 43.227215600001045 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 1.0583588619712851,
            "unit": "iter/sec",
            "range": "stddev: 0.031025903294285225",
            "extra": "mean: 944.8590982999974 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 15.534919193292604,
            "unit": "iter/sec",
            "range": "stddev: 0.028683499062824434",
            "extra": "mean: 64.37111049999942 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 157.17806278335118,
            "unit": "iter/sec",
            "range": "stddev: 0.00007113036951915256",
            "extra": "mean: 6.362211000006823 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 177.01337266993363,
            "unit": "iter/sec",
            "range": "stddev: 0.0012422171409152915",
            "extra": "mean: 5.64929070000062 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "committer": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "distinct": true,
          "id": "504a80538880e0bff03e37369c0b00371768d8f1",
          "message": "Fixes indentation in docstrings",
          "timestamp": "2022-07-25T14:11:11+02:00",
          "tree_id": "07a37d83dbd51c77028634c6c673931b19619208",
          "url": "https://github.com/PyEllips/pyElli/commit/504a80538880e0bff03e37369c0b00371768d8f1"
        },
        "date": 1658751217219,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 19.747932258191028,
            "unit": "iter/sec",
            "range": "stddev: 0.006712999881349211",
            "extra": "mean: 50.63821300000768 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 0.9023509338152891,
            "unit": "iter/sec",
            "range": "stddev: 0.05839603257101975",
            "extra": "mean: 1.1082162853999988 sec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 9.902210061093928,
            "unit": "iter/sec",
            "range": "stddev: 0.0577705542104945",
            "extra": "mean: 100.98755669999662 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 129.1245896436887,
            "unit": "iter/sec",
            "range": "stddev: 0.00022778494859338635",
            "extra": "mean: 7.744458299998769 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 123.36635040429681,
            "unit": "iter/sec",
            "range": "stddev: 0.0021794383758671904",
            "extra": "mean: 8.105938099998866 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "committer": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "distinct": true,
          "id": "e69e5ac0cf09454ddf9a0c8e9722fd76bb9c966a",
          "message": "Fixes indentation in calc_rho",
          "timestamp": "2022-07-25T14:15:15+02:00",
          "tree_id": "71721f07c49599d1228bca6581bfe17cd2e2022b",
          "url": "https://github.com/PyEllips/pyElli/commit/e69e5ac0cf09454ddf9a0c8e9722fd76bb9c966a"
        },
        "date": 1658751442792,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 22.097499661944134,
            "unit": "iter/sec",
            "range": "stddev: 0.005630923901350882",
            "extra": "mean: 45.25398870000572 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 1.065434423284223,
            "unit": "iter/sec",
            "range": "stddev: 0.020326048134480714",
            "extra": "mean: 938.584278999997 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 10.775631600499766,
            "unit": "iter/sec",
            "range": "stddev: 0.03052973647446909",
            "extra": "mean: 92.80198480000195 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 155.91401747325787,
            "unit": "iter/sec",
            "range": "stddev: 0.00019555384464661424",
            "extra": "mean: 6.413791499994659 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 167.8985466988714,
            "unit": "iter/sec",
            "range": "stddev: 0.0016159215001955527",
            "extra": "mean: 5.955977699994719 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "committer": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "distinct": true,
          "id": "6fcc1f6ebad8b44dba3b9bc31c42d1dc97d12376",
          "message": "Sphinx linting",
          "timestamp": "2022-07-25T17:18:05+02:00",
          "tree_id": "cc8860e562a7aaf1412bc350b439cdddfd9a9767",
          "url": "https://github.com/PyEllips/pyElli/commit/6fcc1f6ebad8b44dba3b9bc31c42d1dc97d12376"
        },
        "date": 1658762413073,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 21.970580952689225,
            "unit": "iter/sec",
            "range": "stddev: 0.005097776555756023",
            "extra": "mean: 45.51541000000725 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 1.0338877085786091,
            "unit": "iter/sec",
            "range": "stddev: 0.09080473697106681",
            "extra": "mean: 967.2230279000047 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 8.058721420907979,
            "unit": "iter/sec",
            "range": "stddev: 0.03077190251931759",
            "extra": "mean: 124.0891634999997 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 153.76310284595263,
            "unit": "iter/sec",
            "range": "stddev: 0.000209225918862267",
            "extra": "mean: 6.503510799998935 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 174.4656048736477,
            "unit": "iter/sec",
            "range": "stddev: 0.0012815694327744489",
            "extra": "mean: 5.731788800000004 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "committer": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "distinct": true,
          "id": "85286d1a5634d3e77892fec635f6cabb17066227",
          "message": "Fixes calc_rho indentation",
          "timestamp": "2022-07-25T17:21:10+02:00",
          "tree_id": "898012815d1c133e069e207f4aa0d9bbc3d5f6a8",
          "url": "https://github.com/PyEllips/pyElli/commit/85286d1a5634d3e77892fec635f6cabb17066227"
        },
        "date": 1658762603350,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 22.146939067342238,
            "unit": "iter/sec",
            "range": "stddev: 0.0034152347375716635",
            "extra": "mean: 45.15296660000274 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 1.074589873066017,
            "unit": "iter/sec",
            "range": "stddev: 0.016103395590847194",
            "extra": "mean: 930.5875898000068 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 9.163192090366488,
            "unit": "iter/sec",
            "range": "stddev: 0.03268543804854417",
            "extra": "mean: 109.13227509999786 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 153.20847659602583,
            "unit": "iter/sec",
            "range": "stddev: 0.00023178642055775612",
            "extra": "mean: 6.527054000000021 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 170.29759590046396,
            "unit": "iter/sec",
            "range": "stddev: 0.0015120652745812234",
            "extra": "mean: 5.872073499995167 msec\nrounds: 10"
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
          "id": "f6c0ab06bf6d0567570eed1a1527d350af9ab9e6",
          "message": "Prevent VaryingMixtureLayer from changing Material objects\n\nFixes #70",
          "timestamp": "2022-07-25T19:57:42+02:00",
          "tree_id": "a89f25773f720ff51f07c7c84a63f45de649c6f0",
          "url": "https://github.com/PyEllips/pyElli/commit/f6c0ab06bf6d0567570eed1a1527d350af9ab9e6"
        },
        "date": 1658772025532,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 15.438456240707666,
            "unit": "iter/sec",
            "range": "stddev: 0.005682170439255863",
            "extra": "mean: 64.77331570000047 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 0.597884569575091,
            "unit": "iter/sec",
            "range": "stddev: 0.034839568652778506",
            "extra": "mean: 1.6725636533999988 sec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 11.984083626948893,
            "unit": "iter/sec",
            "range": "stddev: 0.04610723359773718",
            "extra": "mean: 83.44401049999988 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 93.80015142338391,
            "unit": "iter/sec",
            "range": "stddev: 0.0008562850465163276",
            "extra": "mean: 10.6609636000087 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 111.54182739896595,
            "unit": "iter/sec",
            "range": "stddev: 0.0016113917294428074",
            "extra": "mean: 8.965246699995078 msec\nrounds: 10"
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
          "id": "1db9e24cb9f05a8c6324b6b73a1e9d9cc67fc33f",
          "message": "Docs: autosectionlabel",
          "timestamp": "2022-07-25T22:57:11+02:00",
          "tree_id": "7aff50dda455c04e3be40fcd1c8300a78ac161ac",
          "url": "https://github.com/PyEllips/pyElli/commit/1db9e24cb9f05a8c6324b6b73a1e9d9cc67fc33f"
        },
        "date": 1658782763148,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 23.095270830587875,
            "unit": "iter/sec",
            "range": "stddev: 0.003879565924173911",
            "extra": "mean: 43.298907699994515 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 1.049241961263605,
            "unit": "iter/sec",
            "range": "stddev: 0.03692030771080308",
            "extra": "mean: 953.0690126000081 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 10.763648401699491,
            "unit": "iter/sec",
            "range": "stddev: 0.04786035232889165",
            "extra": "mean: 92.90530150001075 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 156.3320841148166,
            "unit": "iter/sec",
            "range": "stddev: 0.00013404331088048369",
            "extra": "mean: 6.39663960000405 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 173.6631286452052,
            "unit": "iter/sec",
            "range": "stddev: 0.0012704733588417665",
            "extra": "mean: 5.758274699996946 msec\nrounds: 10"
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
          "id": "2144c1f8729e8fbfdc1878b14681fc247683912d",
          "message": "Docs: More hyperlinks",
          "timestamp": "2022-07-25T22:59:03+02:00",
          "tree_id": "6ad61ad600913595052fa34d343d1b5d508c8ea9",
          "url": "https://github.com/PyEllips/pyElli/commit/2144c1f8729e8fbfdc1878b14681fc247683912d"
        },
        "date": 1658782868518,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 22.598899933006756,
            "unit": "iter/sec",
            "range": "stddev: 0.006087180220100962",
            "extra": "mean: 44.2499415000043 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 1.1597195797963336,
            "unit": "iter/sec",
            "range": "stddev: 0.04222665640941348",
            "extra": "mean: 862.2774137999954 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 10.711308349283993,
            "unit": "iter/sec",
            "range": "stddev: 0.040003304988530455",
            "extra": "mean: 93.35927670001638 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 143.14112872188747,
            "unit": "iter/sec",
            "range": "stddev: 0.0014960237320622823",
            "extra": "mean: 6.986112300000968 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 171.049894330978,
            "unit": "iter/sec",
            "range": "stddev: 0.0013564900909815028",
            "extra": "mean: 5.846247399983895 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "committer": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "distinct": true,
          "id": "cb8ee6d20feb56e4ecdae7ad04e95bbdcfdc85f7",
          "message": "Fixes sphinx version to avoid bugn in napoleon",
          "timestamp": "2022-07-25T22:59:23+02:00",
          "tree_id": "3979fd77b7469f51d6cb63120489f0eb70648782",
          "url": "https://github.com/PyEllips/pyElli/commit/cb8ee6d20feb56e4ecdae7ad04e95bbdcfdc85f7"
        },
        "date": 1658782908894,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 17.004139346549174,
            "unit": "iter/sec",
            "range": "stddev: 0.006283300881843838",
            "extra": "mean: 58.80920989999652 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 0.6255522103579768,
            "unit": "iter/sec",
            "range": "stddev: 0.058084926958237554",
            "extra": "mean: 1.5985875894000003 sec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 10.855354743879374,
            "unit": "iter/sec",
            "range": "stddev: 0.05178994597070938",
            "extra": "mean: 92.12043490000497 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 103.7559638149639,
            "unit": "iter/sec",
            "range": "stddev: 0.00045061326760322597",
            "extra": "mean: 9.638000200001784 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 126.58609368977086,
            "unit": "iter/sec",
            "range": "stddev: 0.0015198048604026671",
            "extra": "mean: 7.89976189999777 msec\nrounds: 10"
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
          "id": "4b35e54b4019f582ba335afda379e9fb7cf0528d",
          "message": "Docs: Use \\varepsilon instead of \\epsilon",
          "timestamp": "2022-07-25T23:03:08+02:00",
          "tree_id": "c5abf7858994ab65e27b7b48376f047b52a93c4e",
          "url": "https://github.com/PyEllips/pyElli/commit/4b35e54b4019f582ba335afda379e9fb7cf0528d"
        },
        "date": 1658783118387,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 22.029082486289198,
            "unit": "iter/sec",
            "range": "stddev: 0.00462011590617494",
            "extra": "mean: 45.39453700000422 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 1.089332564930921,
            "unit": "iter/sec",
            "range": "stddev: 0.029114014087146433",
            "extra": "mean: 917.9933036000023 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 9.936530540348583,
            "unit": "iter/sec",
            "range": "stddev: 0.03792130131087081",
            "extra": "mean: 100.63874869999836 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 145.6798289800287,
            "unit": "iter/sec",
            "range": "stddev: 0.0012711311638057144",
            "extra": "mean: 6.8643683000004785 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 175.66957424430817,
            "unit": "iter/sec",
            "range": "stddev: 0.0012506622125410662",
            "extra": "mean: 5.692505399991887 msec\nrounds: 10"
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
          "id": "b05900297009dd957777753bbff793f613f8876f",
          "message": "Docs: MixtureMaterials",
          "timestamp": "2022-07-25T23:03:45+02:00",
          "tree_id": "3eb71c0dd8f512c5486f8dafe57c7611209566d6",
          "url": "https://github.com/PyEllips/pyElli/commit/b05900297009dd957777753bbff793f613f8876f"
        },
        "date": 1658783170188,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 19.31283406809657,
            "unit": "iter/sec",
            "range": "stddev: 0.00679572931892662",
            "extra": "mean: 51.779039599989574 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 0.9006565715975656,
            "unit": "iter/sec",
            "range": "stddev: 0.03815453513958686",
            "extra": "mean: 1.1103011197999932 sec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 9.22485542573764,
            "unit": "iter/sec",
            "range": "stddev: 0.05034443451478443",
            "extra": "mean: 108.4027828999865 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 135.19271078763566,
            "unit": "iter/sec",
            "range": "stddev: 0.0002154467502050256",
            "extra": "mean: 7.396848499996622 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 148.49722001349934,
            "unit": "iter/sec",
            "range": "stddev: 0.001283884158800024",
            "extra": "mean: 6.7341327999884015 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "committer": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "distinct": true,
          "id": "19ad6288a4f0180b3ef5469274d40d8bc32bf669",
          "message": "Introduces black formatting for each file, adds black pre-commit hook and adds linting action",
          "timestamp": "2022-07-26T21:04:46+02:00",
          "tree_id": "c181706e553573aa40e8dfa4ecdc79367567bb95",
          "url": "https://github.com/PyEllips/pyElli/commit/19ad6288a4f0180b3ef5469274d40d8bc32bf669"
        },
        "date": 1658862462685,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 17.4352786676898,
            "unit": "iter/sec",
            "range": "stddev: 0.002011079439113142",
            "extra": "mean: 57.35497660000988 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 0.6120229621333192,
            "unit": "iter/sec",
            "range": "stddev: 0.055721074191323605",
            "extra": "mean: 1.6339256234999993 sec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 12.905113716351336,
            "unit": "iter/sec",
            "range": "stddev: 0.03518762744287216",
            "extra": "mean: 77.48866240000325 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 102.44163805105833,
            "unit": "iter/sec",
            "range": "stddev: 0.0008115596069997696",
            "extra": "mean: 9.761655700015126 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 124.72662574077232,
            "unit": "iter/sec",
            "range": "stddev: 0.0005713188200722214",
            "extra": "mean: 8.017534300000762 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "committer": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "distinct": true,
          "id": "0d27f0c3d0c968512ed51d1e2fe38611f4312729",
          "message": "Fixes python version in linting action",
          "timestamp": "2022-07-26T21:06:03+02:00",
          "tree_id": "08df83a3d36597975291293f3e51029cc17fc734",
          "url": "https://github.com/PyEllips/pyElli/commit/0d27f0c3d0c968512ed51d1e2fe38611f4312729"
        },
        "date": 1658862482184,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 26.840756241099978,
            "unit": "iter/sec",
            "range": "stddev: 0.001033308308530281",
            "extra": "mean: 37.256774399997994 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 1.1058709976652206,
            "unit": "iter/sec",
            "range": "stddev: 0.05569673158178192",
            "extra": "mean: 904.2646042000001 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 9.258911972902556,
            "unit": "iter/sec",
            "range": "stddev: 0.013127227970836734",
            "extra": "mean: 108.0040509000014 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 164.28384719970117,
            "unit": "iter/sec",
            "range": "stddev: 0.00016439813879660605",
            "extra": "mean: 6.087025700003323 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 191.85848886216291,
            "unit": "iter/sec",
            "range": "stddev: 0.00043159054973024584",
            "extra": "mean: 5.212174900003674 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "committer": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "distinct": true,
          "id": "2aa04359e8a7d6cb3832cd546dd374e3dced73ef",
          "message": "Renames black linting job to black-lint",
          "timestamp": "2022-07-26T21:07:19+02:00",
          "tree_id": "9af502fe7df4773cc6d46b3011a3e7ba0085496e",
          "url": "https://github.com/PyEllips/pyElli/commit/2aa04359e8a7d6cb3832cd546dd374e3dced73ef"
        },
        "date": 1658862554613,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 24.780800070041185,
            "unit": "iter/sec",
            "range": "stddev: 0.00099814825123543",
            "extra": "mean: 40.35382219999235 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 1.0725524582776922,
            "unit": "iter/sec",
            "range": "stddev: 0.024951639185968152",
            "extra": "mean: 932.3553288999989 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 9.075995126934902,
            "unit": "iter/sec",
            "range": "stddev: 0.01273949533183016",
            "extra": "mean: 110.18075549999935 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 154.47754397014498,
            "unit": "iter/sec",
            "range": "stddev: 0.0002467283638340959",
            "extra": "mean: 6.473432800001433 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 181.89892509727272,
            "unit": "iter/sec",
            "range": "stddev: 0.00040387385824703053",
            "extra": "mean: 5.497558600004027 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "committer": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "distinct": true,
          "id": "f0321db6496caa0fb4aba3bf9469a0203949ee60",
          "message": "Adds formatting information to contributing guidelines",
          "timestamp": "2022-07-26T21:17:07+02:00",
          "tree_id": "b651f6963f708b06ea7baa1d500ce90a11e398f6",
          "url": "https://github.com/PyEllips/pyElli/commit/f0321db6496caa0fb4aba3bf9469a0203949ee60"
        },
        "date": 1658863144895,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 27.750342940829274,
            "unit": "iter/sec",
            "range": "stddev: 0.000774767299079807",
            "extra": "mean: 36.0355906999871 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 1.129816943284131,
            "unit": "iter/sec",
            "range": "stddev: 0.06652553610782691",
            "extra": "mean: 885.0991356999998 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 8.40153347443825,
            "unit": "iter/sec",
            "range": "stddev: 0.01202065457205172",
            "extra": "mean: 119.02589010000497 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 170.13787343732426,
            "unit": "iter/sec",
            "range": "stddev: 0.00018881387202959136",
            "extra": "mean: 5.877586100007193 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 199.60698183624962,
            "unit": "iter/sec",
            "range": "stddev: 0.00008968700211789506",
            "extra": "mean: 5.009844800019891 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "committer": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "distinct": true,
          "id": "47faf3cdaa75aaa3d175b9f97cee189bb86bc009",
          "message": "Reformats to make pylint happier",
          "timestamp": "2022-07-26T21:38:07+02:00",
          "tree_id": "90fed46150d68c3861b09880acc8b605867a7b6f",
          "url": "https://github.com/PyEllips/pyElli/commit/47faf3cdaa75aaa3d175b9f97cee189bb86bc009"
        },
        "date": 1658864407773,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 23.580622996566223,
            "unit": "iter/sec",
            "range": "stddev: 0.001173124902039468",
            "extra": "mean: 42.40770060000614 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 1.057105457884373,
            "unit": "iter/sec",
            "range": "stddev: 0.037671070287073595",
            "extra": "mean: 945.9794124999974 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 10.652854011390911,
            "unit": "iter/sec",
            "range": "stddev: 0.034230395179959315",
            "extra": "mean: 93.8715577000039 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 155.64236006699727,
            "unit": "iter/sec",
            "range": "stddev: 0.00029861102110652306",
            "extra": "mean: 6.424986099989383 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 184.70946936733202,
            "unit": "iter/sec",
            "range": "stddev: 0.00017285042279827537",
            "extra": "mean: 5.4139076000012665 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "committer": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "distinct": true,
          "id": "5b0a408e4db780f0dddda57c5c351bc5e2e01016",
          "message": "Adds pylint  pre-commit hook",
          "timestamp": "2022-07-26T21:44:39+02:00",
          "tree_id": "2817c856ab8a2f0d27ab0f1fcd64d12ac6011d43",
          "url": "https://github.com/PyEllips/pyElli/commit/5b0a408e4db780f0dddda57c5c351bc5e2e01016"
        },
        "date": 1658864792274,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 24.792189758119918,
            "unit": "iter/sec",
            "range": "stddev: 0.0009513371773261334",
            "extra": "mean: 40.33528339998611 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 1.0959759917305303,
            "unit": "iter/sec",
            "range": "stddev: 0.02236137093287237",
            "extra": "mean: 912.4287462000098 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 8.333040975534061,
            "unit": "iter/sec",
            "range": "stddev: 0.008460286845870411",
            "extra": "mean: 120.00421010001219 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 155.29941470942342,
            "unit": "iter/sec",
            "range": "stddev: 0.00022922750747749395",
            "extra": "mean: 6.439174299987371 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 185.49138681031062,
            "unit": "iter/sec",
            "range": "stddev: 0.00017703429164225387",
            "extra": "mean: 5.391085899975678 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "committer": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "distinct": true,
          "id": "881c3422b90cce4ffc1bd7735244a6019c6109da",
          "message": "Adds pylintrc",
          "timestamp": "2022-07-27T11:18:23+02:00",
          "tree_id": "b28169568cb6e8c0129d1528e3ecd0154e04f616",
          "url": "https://github.com/PyEllips/pyElli/commit/881c3422b90cce4ffc1bd7735244a6019c6109da"
        },
        "date": 1658913681352,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 23.78730510728125,
            "unit": "iter/sec",
            "range": "stddev: 0.0006601157753764064",
            "extra": "mean: 42.039230399996086 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 1.0821176596030038,
            "unit": "iter/sec",
            "range": "stddev: 0.042555408977005674",
            "extra": "mean: 924.1139271000065 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 9.255975376322056,
            "unit": "iter/sec",
            "range": "stddev: 0.02792910438792443",
            "extra": "mean: 108.03831679999121 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 157.512829577164,
            "unit": "iter/sec",
            "range": "stddev: 0.00015151773763917386",
            "extra": "mean: 6.348689200012814 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 190.77260386404166,
            "unit": "iter/sec",
            "range": "stddev: 0.00009720511284164155",
            "extra": "mean: 5.241842799989627 msec\nrounds: 10"
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
          "id": "cc1a5acecb2c5673f6dd2fa3546c0c2a284c7043",
          "message": "readability improvements",
          "timestamp": "2022-07-28T11:51:47+02:00",
          "tree_id": "288653914094817bde36f2a498a86f1167cf9f6a",
          "url": "https://github.com/PyEllips/pyElli/commit/cc1a5acecb2c5673f6dd2fa3546c0c2a284c7043"
        },
        "date": 1659002068763,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 17.071740019963922,
            "unit": "iter/sec",
            "range": "stddev: 0.004600629377283802",
            "extra": "mean: 58.57633719999171 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 0.6239480029986684,
            "unit": "iter/sec",
            "range": "stddev: 0.042112900026789434",
            "extra": "mean: 1.6026976529999957 sec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 11.127455649612655,
            "unit": "iter/sec",
            "range": "stddev: 0.040369120926483856",
            "extra": "mean: 89.86780370001384 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 88.24775521976562,
            "unit": "iter/sec",
            "range": "stddev: 0.0032461777022939884",
            "extra": "mean: 11.331733000002941 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 114.40689145013665,
            "unit": "iter/sec",
            "range": "stddev: 0.0016486073684152064",
            "extra": "mean: 8.740732199999002 msec\nrounds: 10"
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
          "id": "1b2083c7a2568b99dcc49218ef0b15726dba925b",
          "message": "Update pylintrc regex for private names",
          "timestamp": "2022-07-28T11:52:29+02:00",
          "tree_id": "0c49fe9466442123a59f64530017cafdec16dedc",
          "url": "https://github.com/PyEllips/pyElli/commit/1b2083c7a2568b99dcc49218ef0b15726dba925b"
        },
        "date": 1659002094839,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 19.218863957652356,
            "unit": "iter/sec",
            "range": "stddev: 0.0027369410052917867",
            "extra": "mean: 52.032211800002415 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 0.6603577691829272,
            "unit": "iter/sec",
            "range": "stddev: 0.049635403472603486",
            "extra": "mean: 1.5143306350999979 sec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 9.32567485910685,
            "unit": "iter/sec",
            "range": "stddev: 0.0462060005428787",
            "extra": "mean: 107.23084549998703 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 84.59485838873093,
            "unit": "iter/sec",
            "range": "stddev: 0.004025691194380561",
            "extra": "mean: 11.821049400009542 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 120.48923545547349,
            "unit": "iter/sec",
            "range": "stddev: 0.0018587737778835085",
            "extra": "mean: 8.299496600005796 msec\nrounds: 10"
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
          "id": "cce5867884d402ced30e13db151947ca394f60e1",
          "message": "Fix linter warnings regarding InhomogeneousLayers init",
          "timestamp": "2022-07-29T09:15:33+02:00",
          "tree_id": "576825c80b19c87bab55b907dbf4d67ee75adf91",
          "url": "https://github.com/PyEllips/pyElli/commit/cce5867884d402ced30e13db151947ca394f60e1"
        },
        "date": 1659079064524,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 21.22160149956984,
            "unit": "iter/sec",
            "range": "stddev: 0.0007121151902788922",
            "extra": "mean: 47.1217971000101 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 0.92793008711341,
            "unit": "iter/sec",
            "range": "stddev: 0.05948480316516988",
            "extra": "mean: 1.0776673952999887 sec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 7.089071848381366,
            "unit": "iter/sec",
            "range": "stddev: 0.014270113042312509",
            "extra": "mean: 141.0621899999967 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 136.16492655402922,
            "unit": "iter/sec",
            "range": "stddev: 0.00026057466615173535",
            "extra": "mean: 7.344035099987423 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 157.44322530416758,
            "unit": "iter/sec",
            "range": "stddev: 0.00022113697655075975",
            "extra": "mean: 6.351495899986048 msec\nrounds: 10"
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
          "id": "646670cf25d9684179e00248facedda1b582bbcb",
          "message": "Docs: Materials",
          "timestamp": "2022-07-29T09:16:01+02:00",
          "tree_id": "33522e9489db0d6ec7de032849cd2d405020c2c1",
          "url": "https://github.com/PyEllips/pyElli/commit/646670cf25d9684179e00248facedda1b582bbcb"
        },
        "date": 1659079107396,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 17.29514059887609,
            "unit": "iter/sec",
            "range": "stddev: 0.0018282373431735934",
            "extra": "mean: 57.81970919999253 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 0.5920857652828353,
            "unit": "iter/sec",
            "range": "stddev: 0.0570166892470315",
            "extra": "mean: 1.688944505400002 sec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 12.476838387118848,
            "unit": "iter/sec",
            "range": "stddev: 0.03910764801365024",
            "extra": "mean: 80.14850950000323 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 93.80360934903128,
            "unit": "iter/sec",
            "range": "stddev: 0.002495430377176146",
            "extra": "mean: 10.66057059999821 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 117.02204408612289,
            "unit": "iter/sec",
            "range": "stddev: 0.0008266455263416876",
            "extra": "mean: 8.545398499995827 msec\nrounds: 10"
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
          "id": "c8726ddc774e446493875f45bd8d210c38fa48fd",
          "message": "Clean up AbstractLayer",
          "timestamp": "2022-07-29T10:16:36+02:00",
          "tree_id": "a6b47647882fe80414bbe5d568d67924edfd5a6a",
          "url": "https://github.com/PyEllips/pyElli/commit/c8726ddc774e446493875f45bd8d210c38fa48fd"
        },
        "date": 1659082717866,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 23.847510565888747,
            "unit": "iter/sec",
            "range": "stddev: 0.0008073053320538337",
            "extra": "mean: 41.93309809999164 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 1.1121691441864505,
            "unit": "iter/sec",
            "range": "stddev: 0.03794928203648031",
            "extra": "mean: 899.1438085000084 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 9.550304396659785,
            "unit": "iter/sec",
            "range": "stddev: 0.03217248203130296",
            "extra": "mean: 104.70870440001363 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 152.57344252362327,
            "unit": "iter/sec",
            "range": "stddev: 0.0007576144626791221",
            "extra": "mean: 6.554220599991822 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 190.97240954771175,
            "unit": "iter/sec",
            "range": "stddev: 0.00007273284914405006",
            "extra": "mean: 5.236358499996641 msec\nrounds: 10"
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
          "id": "4bcc056ba2e45ed9713c5440fe25f75949ecd65a",
          "message": "Docs: Structure",
          "timestamp": "2022-07-29T11:38:04+02:00",
          "tree_id": "c199b5550c7cdf9b08c2960a98348dc5439d1952",
          "url": "https://github.com/PyEllips/pyElli/commit/4bcc056ba2e45ed9713c5440fe25f75949ecd65a"
        },
        "date": 1659087664770,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 23.94877906022317,
            "unit": "iter/sec",
            "range": "stddev: 0.0005515618363243832",
            "extra": "mean: 41.75578210001163 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 1.134292966250369,
            "unit": "iter/sec",
            "range": "stddev: 0.02299361789062694",
            "extra": "mean: 881.6064542000106 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 9.145068297043023,
            "unit": "iter/sec",
            "range": "stddev: 0.028034811942474078",
            "extra": "mean: 109.34855460000676 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 158.2575915136915,
            "unit": "iter/sec",
            "range": "stddev: 0.00030949827014807954",
            "extra": "mean: 6.318812200004231 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 191.82966385235363,
            "unit": "iter/sec",
            "range": "stddev: 0.00008130401297100987",
            "extra": "mean: 5.212958100003107 msec\nrounds: 10"
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
          "id": "2edbc481bfda18fe1bcef78cff32cb9ef3bb79f9",
          "message": "Fix linting",
          "timestamp": "2022-07-29T11:40:58+02:00",
          "tree_id": "b9ae084ee40e0646e98aa1bc4ec2607ddc3a66ec",
          "url": "https://github.com/PyEllips/pyElli/commit/2edbc481bfda18fe1bcef78cff32cb9ef3bb79f9"
        },
        "date": 1659087793831,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 19.83275340511575,
            "unit": "iter/sec",
            "range": "stddev: 0.0010038782663884752",
            "extra": "mean: 50.421642399993516 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 0.8977931705909178,
            "unit": "iter/sec",
            "range": "stddev: 0.024704086737081257",
            "extra": "mean: 1.1138422888000037 sec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 6.514162068119389,
            "unit": "iter/sec",
            "range": "stddev: 0.020945128166768478",
            "extra": "mean: 153.51168569999913 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 102.49083160575559,
            "unit": "iter/sec",
            "range": "stddev: 0.00418238788327329",
            "extra": "mean: 9.756970300003331 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 133.95987438264683,
            "unit": "iter/sec",
            "range": "stddev: 0.0006677949419298629",
            "extra": "mean: 7.464921899997989 msec\nrounds: 10"
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
          "id": "2f34100a5cd244f81b1f0a8af1f58641dfe77c0f",
          "message": "Include Layer in overview graph",
          "timestamp": "2022-07-29T12:02:39+02:00",
          "tree_id": "47b4b7d1dc93fd729b841c7e048f56f8d9cffc9b",
          "url": "https://github.com/PyEllips/pyElli/commit/2f34100a5cd244f81b1f0a8af1f58641dfe77c0f"
        },
        "date": 1659089095960,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 21.222278902215486,
            "unit": "iter/sec",
            "range": "stddev: 0.0008417141896825939",
            "extra": "mean: 47.12029299999472 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 0.9080073036580846,
            "unit": "iter/sec",
            "range": "stddev: 0.06859848690351865",
            "extra": "mean: 1.1013127272999952 sec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 7.520246488893309,
            "unit": "iter/sec",
            "range": "stddev: 0.018022715826797583",
            "extra": "mean: 132.9743647999976 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 131.58241525769748,
            "unit": "iter/sec",
            "range": "stddev: 0.00015498522039392136",
            "extra": "mean: 7.599799699994492 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 151.84426245076526,
            "unit": "iter/sec",
            "range": "stddev: 0.000259719375292658",
            "extra": "mean: 6.5856949999954395 msec\nrounds: 10"
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
          "id": "3c4fd4da52d6784d88d08e5b755076ab0f04525c",
          "message": "Docs: experiment",
          "timestamp": "2022-07-29T13:54:18+02:00",
          "tree_id": "2325efc1a191380e51053a1e6cb759d78ed24734",
          "url": "https://github.com/PyEllips/pyElli/commit/3c4fd4da52d6784d88d08e5b755076ab0f04525c"
        },
        "date": 1659095802517,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 18.050342506329898,
            "unit": "iter/sec",
            "range": "stddev: 0.0012919773980512917",
            "extra": "mean: 55.40061080000669 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 0.6529067101141252,
            "unit": "iter/sec",
            "range": "stddev: 0.054594871192005026",
            "extra": "mean: 1.5316123797000103 sec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 13.026515455273579,
            "unit": "iter/sec",
            "range": "stddev: 0.0350840462982595",
            "extra": "mean: 76.76650010000685 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 108.81495120905554,
            "unit": "iter/sec",
            "range": "stddev: 0.00019304606270023904",
            "extra": "mean: 9.189913600005184 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 129.2456300920415,
            "unit": "iter/sec",
            "range": "stddev: 0.0001569951585979786",
            "extra": "mean: 7.737205500006894 msec\nrounds: 10"
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
          "id": "6e874ef167a0563600939bb4ebc1f4b65bbd2a38",
          "message": "Cleanup experiment code",
          "timestamp": "2022-07-29T13:54:36+02:00",
          "tree_id": "372a6469fe0263837d76e7335f8f6c2fdf9fd350",
          "url": "https://github.com/PyEllips/pyElli/commit/6e874ef167a0563600939bb4ebc1f4b65bbd2a38"
        },
        "date": 1659095846175,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 16.291423989948335,
            "unit": "iter/sec",
            "range": "stddev: 0.005455181748789737",
            "extra": "mean: 61.381988500022544 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 0.5611315450632913,
            "unit": "iter/sec",
            "range": "stddev: 0.040790090868938964",
            "extra": "mean: 1.7821133186999987 sec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 7.968072919851607,
            "unit": "iter/sec",
            "range": "stddev: 0.040190833369652665",
            "extra": "mean: 125.50085949999357 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 90.16198411902,
            "unit": "iter/sec",
            "range": "stddev: 0.0022418765398550537",
            "extra": "mean: 11.091149000003497 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 100.52650050945692,
            "unit": "iter/sec",
            "range": "stddev: 0.0022586862699073627",
            "extra": "mean: 9.947625700010576 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "committer": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "distinct": true,
          "id": "cc16de1142477492a5ea1a02edfcb03b491b8d82",
          "message": "Disables display of ipywidgets if not in an interactive shell",
          "timestamp": "2022-07-29T20:07:33+02:00",
          "tree_id": "40c7129eb7b36842d7531367f1a43bef0bccf95b",
          "url": "https://github.com/PyEllips/pyElli/commit/cc16de1142477492a5ea1a02edfcb03b491b8d82"
        },
        "date": 1659118220840,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 20.527155457089528,
            "unit": "iter/sec",
            "range": "stddev: 0.0015480593013238167",
            "extra": "mean: 48.71595589999913 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 5.427251159169339,
            "unit": "iter/sec",
            "range": "stddev: 0.01775787714938901",
            "extra": "mean: 184.255338600002 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 7.458352874528624,
            "unit": "iter/sec",
            "range": "stddev: 0.015140909664639752",
            "extra": "mean: 134.0778610000001 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 127.01962957547038,
            "unit": "iter/sec",
            "range": "stddev: 0.00042003699795665366",
            "extra": "mean: 7.872798899998656 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 152.24334759358544,
            "unit": "iter/sec",
            "range": "stddev: 0.00022900113966176845",
            "extra": "mean: 6.568431500005545 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "committer": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "distinct": true,
          "id": "df0c2acb03e82474b26413c8eb7267dfbbd6613e",
          "message": "Adds examples to dockerfile & adds read_write docs",
          "timestamp": "2022-07-29T20:24:14+02:00",
          "tree_id": "425c1c666ac33003fa8f11981bfec4a3577787d3",
          "url": "https://github.com/PyEllips/pyElli/commit/df0c2acb03e82474b26413c8eb7267dfbbd6613e"
        },
        "date": 1659119166231,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 25.065910623994817,
            "unit": "iter/sec",
            "range": "stddev: 0.000779655831779984",
            "extra": "mean: 39.89482029999465 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 6.473602243205496,
            "unit": "iter/sec",
            "range": "stddev: 0.019221825861158524",
            "extra": "mean: 154.4735006000053 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 8.451797159383498,
            "unit": "iter/sec",
            "range": "stddev: 0.009587608801126262",
            "extra": "mean: 118.31803119999904 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 156.44294793211841,
            "unit": "iter/sec",
            "range": "stddev: 0.0003222940710929374",
            "extra": "mean: 6.39210659999776 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 144.53574381953817,
            "unit": "iter/sec",
            "range": "stddev: 0.0032058178013407586",
            "extra": "mean: 6.918703799999548 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "committer": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "distinct": true,
          "id": "fa7c5cd650d01f89e12563e4a5f63ebab7cefd63",
          "message": "Fix sphinx-lint",
          "timestamp": "2022-07-29T20:26:30+02:00",
          "tree_id": "f725b596163d3f7518332d977a02b810cf6ea480",
          "url": "https://github.com/PyEllips/pyElli/commit/fa7c5cd650d01f89e12563e4a5f63ebab7cefd63"
        },
        "date": 1659119294494,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 26.26604400558425,
            "unit": "iter/sec",
            "range": "stddev: 0.0005881804792015838",
            "extra": "mean: 38.071968499991726 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 5.97178325841455,
            "unit": "iter/sec",
            "range": "stddev: 0.029261468068192038",
            "extra": "mean: 167.45416849999515 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 8.716402357991985,
            "unit": "iter/sec",
            "range": "stddev: 0.012106865230285849",
            "extra": "mean: 114.72623210000279 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 152.73555488217113,
            "unit": "iter/sec",
            "range": "stddev: 0.00020970193018534953",
            "extra": "mean: 6.547263999999586 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 183.2220055048558,
            "unit": "iter/sec",
            "range": "stddev: 0.0001435023298141373",
            "extra": "mean: 5.457859700010204 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "committer": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "distinct": true,
          "id": "95bdd970a9e41dee86a6f8c8d83ef4218178b52f",
          "message": "Renames LorentzLambda param to lbda (fixes #73)",
          "timestamp": "2022-07-30T11:03:24+02:00",
          "tree_id": "a526167020284b9bbdab16eab2e1226575f915e4",
          "url": "https://github.com/PyEllips/pyElli/commit/95bdd970a9e41dee86a6f8c8d83ef4218178b52f"
        },
        "date": 1659171914060,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 24.224713246244097,
            "unit": "iter/sec",
            "range": "stddev: 0.0006312317105867735",
            "extra": "mean: 41.28015840001922 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 7.741551097379322,
            "unit": "iter/sec",
            "range": "stddev: 0.022183874503024666",
            "extra": "mean: 129.17308009999715 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 8.959901146915447,
            "unit": "iter/sec",
            "range": "stddev: 0.020136709968915263",
            "extra": "mean: 111.60837420000576 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 159.31086199456064,
            "unit": "iter/sec",
            "range": "stddev: 0.00014181956652658346",
            "extra": "mean: 6.277035900001238 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 187.34327564107835,
            "unit": "iter/sec",
            "range": "stddev: 0.00028712440177353776",
            "extra": "mean: 5.337794999996959 msec\nrounds: 10"
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
          "id": "4557add95c7e6a53db2864645d2b8e43ac8eaffc",
          "message": "Fix #73 everywhere",
          "timestamp": "2022-07-30T14:06:41+02:00",
          "tree_id": "8386abb29213ce6af3dcad8697b2e6bfd110222f",
          "url": "https://github.com/PyEllips/pyElli/commit/4557add95c7e6a53db2864645d2b8e43ac8eaffc"
        },
        "date": 1659182929835,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 20.09302875401494,
            "unit": "iter/sec",
            "range": "stddev: 0.0014090312721491455",
            "extra": "mean: 49.768504899998334 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 5.55426221782652,
            "unit": "iter/sec",
            "range": "stddev: 0.0116928025476096",
            "extra": "mean: 180.04191390000983 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 7.289163557271487,
            "unit": "iter/sec",
            "range": "stddev: 0.017912721019733516",
            "extra": "mean: 137.18995219999215 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 129.65858431235463,
            "unit": "iter/sec",
            "range": "stddev: 0.00011461020687566956",
            "extra": "mean: 7.7125630000011824 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 138.0634497091047,
            "unit": "iter/sec",
            "range": "stddev: 0.001298160015626188",
            "extra": "mean: 7.243046600001435 msec\nrounds: 10"
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
          "id": "37674612e779acaebc8fb8523d32171a8ab1f13d",
          "message": "Update create_dispersion_prototypes.py",
          "timestamp": "2022-07-30T14:10:04+02:00",
          "tree_id": "e25e0fda442f456743422a015bef4b9ba0d0cfa3",
          "url": "https://github.com/PyEllips/pyElli/commit/37674612e779acaebc8fb8523d32171a8ab1f13d"
        },
        "date": 1659183134202,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 20.160051251687307,
            "unit": "iter/sec",
            "range": "stddev: 0.0009180936463626779",
            "extra": "mean: 49.60304850000341 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 5.0578764149188515,
            "unit": "iter/sec",
            "range": "stddev: 0.027770909621228086",
            "extra": "mean: 197.71143420000783 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 7.656461189365184,
            "unit": "iter/sec",
            "range": "stddev: 0.014815350814290211",
            "extra": "mean: 130.60864220000212 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 127.16223808486333,
            "unit": "iter/sec",
            "range": "stddev: 0.00029812774857592057",
            "extra": "mean: 7.863969800001768 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 149.8976985680774,
            "unit": "iter/sec",
            "range": "stddev: 0.0003662488623726886",
            "extra": "mean: 6.671216500004107 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "committer": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "distinct": true,
          "id": "4862ff7fae87212d7919e7faf70caa08a59b2852",
          "message": "Fixes display error of lambda_r in docs",
          "timestamp": "2022-07-30T14:21:25+02:00",
          "tree_id": "5bcef6e999b29def7694c274e9c526fb28ec600b",
          "url": "https://github.com/PyEllips/pyElli/commit/4862ff7fae87212d7919e7faf70caa08a59b2852"
        },
        "date": 1659183798141,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 25.3481105449949,
            "unit": "iter/sec",
            "range": "stddev: 0.0007198629546787942",
            "extra": "mean: 39.45067220000169 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 6.636454081157218,
            "unit": "iter/sec",
            "range": "stddev: 0.027453934006855",
            "extra": "mean: 150.68287790000454 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 8.686242058208503,
            "unit": "iter/sec",
            "range": "stddev: 0.009341384408085806",
            "extra": "mean: 115.124583599993 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 153.5721645661684,
            "unit": "iter/sec",
            "range": "stddev: 0.00025381831685716534",
            "extra": "mean: 6.511596699994016 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 181.99391183058168,
            "unit": "iter/sec",
            "range": "stddev: 0.00014181755968689628",
            "extra": "mean: 5.49468929999648 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "github@schroedingerscat.org",
            "name": "Florian Dobener",
            "username": "domna"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "dde99562186fe63ae5e65c0e0d675da067de1f52",
          "message": "Adds code style black badge",
          "timestamp": "2022-07-30T14:24:52+02:00",
          "tree_id": "68e27e7e0e6aa746bedeb58ef674c68949ede443",
          "url": "https://github.com/PyEllips/pyElli/commit/dde99562186fe63ae5e65c0e0d675da067de1f52"
        },
        "date": 1659184042066,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 17.523665561390594,
            "unit": "iter/sec",
            "range": "stddev: 0.001813663440844176",
            "extra": "mean: 57.065686199996435 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 3.969559112033435,
            "unit": "iter/sec",
            "range": "stddev: 0.03196297374103628",
            "extra": "mean: 251.91714539999455 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 11.473719755265892,
            "unit": "iter/sec",
            "range": "stddev: 0.03751641156422004",
            "extra": "mean: 87.15569329999084 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 101.60438092885185,
            "unit": "iter/sec",
            "range": "stddev: 0.0004514890740881982",
            "extra": "mean: 9.842095300007259 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 126.911118039624,
            "unit": "iter/sec",
            "range": "stddev: 0.00024792332124143904",
            "extra": "mean: 7.879530299999261 msec\nrounds: 10"
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
          "id": "2e58912e357f0a93adc4f1747c5c1ad71a035574",
          "message": "Fixing many typos",
          "timestamp": "2022-07-30T14:25:45+02:00",
          "tree_id": "0de17bbfd3f4055c0b82d535c84d36ad0f21a75c",
          "url": "https://github.com/PyEllips/pyElli/commit/2e58912e357f0a93adc4f1747c5c1ad71a035574"
        },
        "date": 1659184062649,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 24.03294632391571,
            "unit": "iter/sec",
            "range": "stddev: 0.0011377510198998387",
            "extra": "mean: 41.60954659998879 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 6.412753302079932,
            "unit": "iter/sec",
            "range": "stddev: 0.018798349442291445",
            "extra": "mean: 155.9392593000041 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 9.65500315959029,
            "unit": "iter/sec",
            "range": "stddev: 0.029198295666073633",
            "extra": "mean: 103.57324419999827 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 159.38418795072428,
            "unit": "iter/sec",
            "range": "stddev: 0.0002595300426426716",
            "extra": "mean: 6.274148099993226 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 193.0012646216735,
            "unit": "iter/sec",
            "range": "stddev: 0.00006103002452924942",
            "extra": "mean: 5.181313199994975 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "committer": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "distinct": true,
          "id": "ff298983444099273a26aa66b5d6f16dafb796a1",
          "message": "Adds MM and multilayer example to gallery and ipynb generation script",
          "timestamp": "2022-07-30T18:42:55+02:00",
          "tree_id": "240714c0774c5203c091f12739d7558dc3bff97d",
          "url": "https://github.com/PyEllips/pyElli/commit/ff298983444099273a26aa66b5d6f16dafb796a1"
        },
        "date": 1659199484440,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 24.171756457021253,
            "unit": "iter/sec",
            "range": "stddev: 0.000778125235870062",
            "extra": "mean: 41.37059720000309 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 8.263707978244547,
            "unit": "iter/sec",
            "range": "stddev: 0.014177413571982947",
            "extra": "mean: 121.01105249999762 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 8.87225189450275,
            "unit": "iter/sec",
            "range": "stddev: 0.031025547247152997",
            "extra": "mean: 112.71095679999803 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 156.97320252369175,
            "unit": "iter/sec",
            "range": "stddev: 0.0002829269568911449",
            "extra": "mean: 6.370514100004243 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 189.81521412983213,
            "unit": "iter/sec",
            "range": "stddev: 0.00008524100211674495",
            "extra": "mean: 5.268281599998659 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "committer": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "distinct": true,
          "id": "53a782bb42acddc81b1da203789024da5352ab69",
          "message": "Adds torch to docs requirements",
          "timestamp": "2022-07-30T18:48:20+02:00",
          "tree_id": "7e381aa84e0dfef245bf2fe2c197d252f33b4cbb",
          "url": "https://github.com/PyEllips/pyElli/commit/53a782bb42acddc81b1da203789024da5352ab69"
        },
        "date": 1659199804799,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 24.236803830435598,
            "unit": "iter/sec",
            "range": "stddev: 0.00075876215951931",
            "extra": "mean: 41.259565700005396 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 6.574654832511474,
            "unit": "iter/sec",
            "range": "stddev: 0.035564620262322544",
            "extra": "mean: 152.09923950000075 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 8.799341657190327,
            "unit": "iter/sec",
            "range": "stddev: 0.02837476785011425",
            "extra": "mean: 113.6448656000141 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 157.77710985445447,
            "unit": "iter/sec",
            "range": "stddev: 0.000301593414423327",
            "extra": "mean: 6.338055000009035 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 190.06844839938296,
            "unit": "iter/sec",
            "range": "stddev: 0.00015577375556614256",
            "extra": "mean: 5.261262500016528 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "committer": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "distinct": true,
          "id": "ffb4286eb94f88704892839c694bae0b9433c5f6",
          "message": "Adds explanatory text to multilayer example",
          "timestamp": "2022-07-30T18:58:24+02:00",
          "tree_id": "b5de9533aed188ceeaf159cb960e68b69e21097a",
          "url": "https://github.com/PyEllips/pyElli/commit/ffb4286eb94f88704892839c694bae0b9433c5f6"
        },
        "date": 1659200419196,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 24.968212407001047,
            "unit": "iter/sec",
            "range": "stddev: 0.0005954829540372371",
            "extra": "mean: 40.05092489999811 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 6.112593023374329,
            "unit": "iter/sec",
            "range": "stddev: 0.018947967550089033",
            "extra": "mean: 163.59669229998417 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 9.008995073472555,
            "unit": "iter/sec",
            "range": "stddev: 0.016500837574222837",
            "extra": "mean: 111.00017170001024 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 158.5572935285717,
            "unit": "iter/sec",
            "range": "stddev: 0.0001580811449042553",
            "extra": "mean: 6.306868499996199 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 186.7736710458608,
            "unit": "iter/sec",
            "range": "stddev: 0.00032498447019251356",
            "extra": "mean: 5.354073700004847 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "committer": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "distinct": true,
          "id": "7caeb9f64aa5e4efe01ceeacf79db3c4b8be97fd",
          "message": "Adds docs for helpers, plots and spectraray",
          "timestamp": "2022-07-31T11:29:10+02:00",
          "tree_id": "a5f89419b55d84013d630d0e05c829f38518687e",
          "url": "https://github.com/PyEllips/pyElli/commit/7caeb9f64aa5e4efe01ceeacf79db3c4b8be97fd"
        },
        "date": 1659259866087,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 25.0911654879458,
            "unit": "iter/sec",
            "range": "stddev: 0.0008257605794329249",
            "extra": "mean: 39.854665200005 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 6.355039888469322,
            "unit": "iter/sec",
            "range": "stddev: 0.02333109783727258",
            "extra": "mean: 157.35542459999579 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 8.738989010392892,
            "unit": "iter/sec",
            "range": "stddev: 0.01327547368882804",
            "extra": "mean: 114.42971250000937 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 156.6963986591023,
            "unit": "iter/sec",
            "range": "stddev: 0.000347984874149966",
            "extra": "mean: 6.381767600004196 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 181.4461413510599,
            "unit": "iter/sec",
            "range": "stddev: 0.000633354875278854",
            "extra": "mean: 5.511277299996209 msec\nrounds: 10"
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
          "id": "bb7b2234e79b89f15987e4f38e38ff29e900246b",
          "message": "Merge pull request #74 from PyEllips/docs-dispersion-plots\n\nDocs dispersion plots",
          "timestamp": "2022-07-31T11:50:08+02:00",
          "tree_id": "33c2091f00354457f9549e9e2f83279958a3fc82",
          "url": "https://github.com/PyEllips/pyElli/commit/bb7b2234e79b89f15987e4f38e38ff29e900246b"
        },
        "date": 1659261114731,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 24.954176147258092,
            "unit": "iter/sec",
            "range": "stddev: 0.0008391941195338685",
            "extra": "mean: 40.07345279999868 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 6.46682446813399,
            "unit": "iter/sec",
            "range": "stddev: 0.027115803326107055",
            "extra": "mean: 154.6354018000045 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 8.889830547152798,
            "unit": "iter/sec",
            "range": "stddev: 0.013631709729332978",
            "extra": "mean: 112.48808340000096 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 160.86723138341918,
            "unit": "iter/sec",
            "range": "stddev: 0.0003008171569888172",
            "extra": "mean: 6.216306400006033 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 193.81333868348395,
            "unit": "iter/sec",
            "range": "stddev: 0.00006263684426787558",
            "extra": "mean: 5.159603600003493 msec\nrounds: 10"
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
          "id": "97aae3fe3b732cfe24d9964db3f71a44e78215a1",
          "message": "Docs: Result documentation",
          "timestamp": "2022-08-05T15:21:15+02:00",
          "tree_id": "d9e2d321f393b181dcc11d658598297dfad49dbf",
          "url": "https://github.com/PyEllips/pyElli/commit/97aae3fe3b732cfe24d9964db3f71a44e78215a1"
        },
        "date": 1659705785580,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 24.168087657579644,
            "unit": "iter/sec",
            "range": "stddev: 0.0006857199415416504",
            "extra": "mean: 41.37687739999478 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 7.485098723471373,
            "unit": "iter/sec",
            "range": "stddev: 0.022883807244445487",
            "extra": "mean: 133.5987722999903 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 9.12214815262918,
            "unit": "iter/sec",
            "range": "stddev: 0.028105405195695456",
            "extra": "mean: 109.62330180000208 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 159.6466521488788,
            "unit": "iter/sec",
            "range": "stddev: 0.00046397550442609984",
            "extra": "mean: 6.263833200006275 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 191.40913683877793,
            "unit": "iter/sec",
            "range": "stddev: 0.0002786017085750458",
            "extra": "mean: 5.224410999994689 msec\nrounds: 10"
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
          "id": "ac5f36b14d526fe35ee4e4b4db49f6a2e942e058",
          "message": "Add transmissive ellipsometric properties",
          "timestamp": "2022-08-05T15:22:35+02:00",
          "tree_id": "ea91e471dd57843fd40341bc1f23e458f1fdcc70",
          "url": "https://github.com/PyEllips/pyElli/commit/ac5f36b14d526fe35ee4e4b4db49f6a2e942e058"
        },
        "date": 1659705868161,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 24.038620389825997,
            "unit": "iter/sec",
            "range": "stddev: 0.000546084207528686",
            "extra": "mean: 41.59972509999932 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 8.331436799774613,
            "unit": "iter/sec",
            "range": "stddev: 0.011135003100204302",
            "extra": "mean: 120.02731629999914 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 8.570995929593492,
            "unit": "iter/sec",
            "range": "stddev: 0.021114661239809887",
            "extra": "mean: 116.6725557000035 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 156.60261770989345,
            "unit": "iter/sec",
            "range": "stddev: 0.00034169256941822936",
            "extra": "mean: 6.385589299998173 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 188.66349010194952,
            "unit": "iter/sec",
            "range": "stddev: 0.00009957366489899097",
            "extra": "mean: 5.300442599994426 msec\nrounds: 10"
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
          "id": "2f79bd566fb58a817f997e6808a4150a507196b9",
          "message": "Reorder properties in Result",
          "timestamp": "2022-08-05T15:24:08+02:00",
          "tree_id": "26a34fda0a1ab6fb82d0df6de07f2d808c162ccd",
          "url": "https://github.com/PyEllips/pyElli/commit/2f79bd566fb58a817f997e6808a4150a507196b9"
        },
        "date": 1659705984919,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 16.794379638592464,
            "unit": "iter/sec",
            "range": "stddev: 0.0033944009647053543",
            "extra": "mean: 59.54372959999432 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 3.636892149530887,
            "unit": "iter/sec",
            "range": "stddev: 0.030803100248265686",
            "extra": "mean: 274.9600369999939 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 15.76887278064356,
            "unit": "iter/sec",
            "range": "stddev: 0.020510669955444063",
            "extra": "mean: 63.41607379999345 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 104.50238711653677,
            "unit": "iter/sec",
            "range": "stddev: 0.0005176543286521827",
            "extra": "mean: 9.56915940001295 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 127.1064913945522,
            "unit": "iter/sec",
            "range": "stddev: 0.00028660799568517225",
            "extra": "mean: 7.867418800003634 msec\nrounds: 10"
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
          "id": "a00a67d0c42f6a6245948d74b8e3b7e4b3508d82",
          "message": "Fix Linting",
          "timestamp": "2022-08-05T15:24:50+02:00",
          "tree_id": "7bcea358f65ff95f74ce5eacf822df63363f82ef",
          "url": "https://github.com/PyEllips/pyElli/commit/a00a67d0c42f6a6245948d74b8e3b7e4b3508d82"
        },
        "date": 1659706005713,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 24.10963108301235,
            "unit": "iter/sec",
            "range": "stddev: 0.002447612974372147",
            "extra": "mean: 41.47720039999285 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 6.438907729422578,
            "unit": "iter/sec",
            "range": "stddev: 0.021489177729636516",
            "extra": "mean: 155.30584410000188 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_torch",
            "value": 8.410317963776693,
            "unit": "iter/sec",
            "range": "stddev: 0.03433448537685792",
            "extra": "mean: 118.90156880001541 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 147.3821822048948,
            "unit": "iter/sec",
            "range": "stddev: 0.0013363219586261534",
            "extra": "mean: 6.785080699984292 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 160.38415983817052,
            "unit": "iter/sec",
            "range": "stddev: 0.002568207392115503",
            "extra": "mean: 6.23502969999663 msec\nrounds: 10"
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
          "id": "cc91f6e612ef543d3551dbeb01fd1fe7bfcc24c8",
          "message": "Use Scipy as only expm solver\n\n* Use Scipy as only expm solver (need scipy >= 1.9.0)\r\n\r\n* Fix linting and tests\r\n\r\n* Fix uniaxial crystal test\r\n\r\n* Fix remaining tests\r\n\r\n* Removes last occurences of PropagatorExpmScipy and bumps scipy version to 1.9.0\r\n\r\nCo-authored-by: domna <florian.dobener@physik.hu-berlin.de>",
          "timestamp": "2022-08-06T17:26:29+02:00",
          "tree_id": "6353c7f4aa001c45ea19755247e2dee1b7433d78",
          "url": "https://github.com/PyEllips/pyElli/commit/cc91f6e612ef543d3551dbeb01fd1fe7bfcc24c8"
        },
        "date": 1659799687797,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 17.121692304781266,
            "unit": "iter/sec",
            "range": "stddev: 0.0038760964335131792",
            "extra": "mean: 58.40544159999581 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 5.191707533512725,
            "unit": "iter/sec",
            "range": "stddev: 0.022848038987202116",
            "extra": "mean: 192.61485619999803 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 58.91919616399765,
            "unit": "iter/sec",
            "range": "stddev: 0.007810082005207756",
            "extra": "mean: 16.972397199998568 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 118.54531854166783,
            "unit": "iter/sec",
            "range": "stddev: 0.0009786941657320845",
            "extra": "mean: 8.435592499998279 msec\nrounds: 10"
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
          "id": "cc91f6e612ef543d3551dbeb01fd1fe7bfcc24c8",
          "message": "Use Scipy as only expm solver\n\n* Use Scipy as only expm solver (need scipy >= 1.9.0)\r\n\r\n* Fix linting and tests\r\n\r\n* Fix uniaxial crystal test\r\n\r\n* Fix remaining tests\r\n\r\n* Removes last occurences of PropagatorExpmScipy and bumps scipy version to 1.9.0\r\n\r\nCo-authored-by: domna <florian.dobener@physik.hu-berlin.de>",
          "timestamp": "2022-08-06T17:26:29+02:00",
          "tree_id": "6353c7f4aa001c45ea19755247e2dee1b7433d78",
          "url": "https://github.com/PyEllips/pyElli/commit/cc91f6e612ef543d3551dbeb01fd1fe7bfcc24c8"
        },
        "date": 1659800038296,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 20.537257363547823,
            "unit": "iter/sec",
            "range": "stddev: 0.0023552152463680613",
            "extra": "mean: 48.691993400001365 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 7.494757580084144,
            "unit": "iter/sec",
            "range": "stddev: 0.01856073431419046",
            "extra": "mean: 133.42659709999225 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 73.70011206253542,
            "unit": "iter/sec",
            "range": "stddev: 0.003488090346911769",
            "extra": "mean: 13.568500399992445 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 154.76744156691336,
            "unit": "iter/sec",
            "range": "stddev: 0.00017616255412545572",
            "extra": "mean: 6.461307300008912 msec\nrounds: 10"
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
          "id": "8e73a77990d4ce467f2742486c322aa0e4a4ee2c",
          "message": "Re-enable older scipy and python versions",
          "timestamp": "2022-08-08T11:09:28+02:00",
          "tree_id": "7328824aa5086268d00221804b155c4303a4dd98",
          "url": "https://github.com/PyEllips/pyElli/commit/8e73a77990d4ce467f2742486c322aa0e4a4ee2c"
        },
        "date": 1659949849802,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 25.142920278882823,
            "unit": "iter/sec",
            "range": "stddev: 0.0008305106428926899",
            "extra": "mean: 39.77262740000356 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 6.8086585443809655,
            "unit": "iter/sec",
            "range": "stddev: 0.021494438750440367",
            "extra": "mean: 146.87180939999962 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 137.2957000511004,
            "unit": "iter/sec",
            "range": "stddev: 0.0013082793330495763",
            "extra": "mean: 7.283549299998526 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 191.36762827479646,
            "unit": "iter/sec",
            "range": "stddev: 0.00005725625738139045",
            "extra": "mean: 5.225544200004606 msec\nrounds: 10"
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
          "id": "579fb7504b67d851ac6c9679178b8c2e4547a5b8",
          "message": "Simplify ResultList",
          "timestamp": "2022-08-08T11:41:51+02:00",
          "tree_id": "dc022a4cb9ccb0f9269b7d5c3552f0f05cd14c7b",
          "url": "https://github.com/PyEllips/pyElli/commit/579fb7504b67d851ac6c9679178b8c2e4547a5b8"
        },
        "date": 1659951802474,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 17.722646735437554,
            "unit": "iter/sec",
            "range": "stddev: 0.006296987765924021",
            "extra": "mean: 56.424980700001015 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 4.186627443962741,
            "unit": "iter/sec",
            "range": "stddev: 0.020639844358516093",
            "extra": "mean: 238.85574090000148 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 74.41766484257595,
            "unit": "iter/sec",
            "range": "stddev: 0.005387272146559724",
            "extra": "mean: 13.437669700002175 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 129.67371965488417,
            "unit": "iter/sec",
            "range": "stddev: 0.0003709551441144475",
            "extra": "mean: 7.711662799998464 msec\nrounds: 10"
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
          "id": "9704a0d679a1d976bcda99c3b5d030af3aa599cf",
          "message": "Simplify Result.__getattr__",
          "timestamp": "2022-08-08T12:16:06+02:00",
          "tree_id": "00df7cdfccb4662d6c9e5672953a733a5be67de6",
          "url": "https://github.com/PyEllips/pyElli/commit/9704a0d679a1d976bcda99c3b5d030af3aa599cf"
        },
        "date": 1659953856154,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 16.270248939006734,
            "unit": "iter/sec",
            "range": "stddev: 0.005216949928082456",
            "extra": "mean: 61.46187459999908 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 3.742840014423573,
            "unit": "iter/sec",
            "range": "stddev: 0.024198042155998214",
            "extra": "mean: 267.1767951999968 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 90.78751899309722,
            "unit": "iter/sec",
            "range": "stddev: 0.002049650313170702",
            "extra": "mean: 11.014729899999054 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 123.4303821170412,
            "unit": "iter/sec",
            "range": "stddev: 0.00027983569280516115",
            "extra": "mean: 8.101732999998035 msec\nrounds: 10"
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
          "id": "a891ccd4412e2545a30debe0401958a7361f1a35",
          "message": "Docs: ResultList",
          "timestamp": "2022-08-09T11:46:35+02:00",
          "tree_id": "71534f52e804804286cba08ad5927f6c0740fdfc",
          "url": "https://github.com/PyEllips/pyElli/commit/a891ccd4412e2545a30debe0401958a7361f1a35"
        },
        "date": 1660038484279,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 23.895212325388087,
            "unit": "iter/sec",
            "range": "stddev: 0.0006965705762770434",
            "extra": "mean: 41.84938750000242 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 7.275749608531885,
            "unit": "iter/sec",
            "range": "stddev: 0.021757766950040218",
            "extra": "mean: 137.44288269999743 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 138.9108329417369,
            "unit": "iter/sec",
            "range": "stddev: 0.0013955464515698092",
            "extra": "mean: 7.1988626000063505 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 190.43443636575012,
            "unit": "iter/sec",
            "range": "stddev: 0.00009034441787579663",
            "extra": "mean: 5.251151100000584 msec\nrounds: 10"
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
          "id": "4328f23dcc6ff08289f960eacfee5b570a3b99bb",
          "message": "Make linter happy",
          "timestamp": "2022-08-10T08:54:40+02:00",
          "tree_id": "66ab272d87671ca84bc09eb54489e8364df5eca1",
          "url": "https://github.com/PyEllips/pyElli/commit/4328f23dcc6ff08289f960eacfee5b570a3b99bb"
        },
        "date": 1660114580103,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 21.004446406046817,
            "unit": "iter/sec",
            "range": "stddev: 0.003784280057984088",
            "extra": "mean: 47.608967200017105 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 5.494430157415215,
            "unit": "iter/sec",
            "range": "stddev: 0.010860377923158483",
            "extra": "mean: 182.00249549999512 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 112.48988589391308,
            "unit": "iter/sec",
            "range": "stddev: 0.0018176950332037007",
            "extra": "mean: 8.88968809998687 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 164.101944722823,
            "unit": "iter/sec",
            "range": "stddev: 0.00018239409517819497",
            "extra": "mean: 6.093773000003466 msec\nrounds: 10"
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
          "id": "8b45ab047fa60cc6d92ee07d5a6f6b399d4ff9d6",
          "message": "Add more conversion functions",
          "timestamp": "2022-08-10T12:59:12+02:00",
          "tree_id": "0d0ce22fa27b1c8c0fa7c4f5ff212311d69caf05",
          "url": "https://github.com/PyEllips/pyElli/commit/8b45ab047fa60cc6d92ee07d5a6f6b399d4ff9d6"
        },
        "date": 1660129239349,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 24.115556712441624,
            "unit": "iter/sec",
            "range": "stddev: 0.0010627591733675286",
            "extra": "mean: 41.46700869999336 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 6.146811202186578,
            "unit": "iter/sec",
            "range": "stddev: 0.022207849421983703",
            "extra": "mean: 162.68597930001079 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 82.0216364875065,
            "unit": "iter/sec",
            "range": "stddev: 0.0041540211733242655",
            "extra": "mean: 12.191904999997405 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 159.96905558578229,
            "unit": "iter/sec",
            "range": "stddev: 0.00009592001066055252",
            "extra": "mean: 6.25120900000411 msec\nrounds: 10"
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
          "id": "5bfe7392037a3ee489c3ae23c5a97028a2df9ce5",
          "message": "Fix and rename conversion functions",
          "timestamp": "2022-08-10T21:39:22+02:00",
          "tree_id": "3d36d3842b419ba2c5b29ba667f9bec81af81245",
          "url": "https://github.com/PyEllips/pyElli/commit/5bfe7392037a3ee489c3ae23c5a97028a2df9ce5"
        },
        "date": 1660160447324,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 24.718796376943065,
            "unit": "iter/sec",
            "range": "stddev: 0.0010580737639503306",
            "extra": "mean: 40.455044199998724 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 6.931391200401088,
            "unit": "iter/sec",
            "range": "stddev: 0.02065015660388302",
            "extra": "mean: 144.27118180000207 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 101.72094029820038,
            "unit": "iter/sec",
            "range": "stddev: 0.0033930481696192276",
            "extra": "mean: 9.830817499999966 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 192.19094370133274,
            "unit": "iter/sec",
            "range": "stddev: 0.00007299673652816679",
            "extra": "mean: 5.203158800000551 msec\nrounds: 10"
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
          "id": "76bfacda6fd2bf4caaac3de53042366a98d0f951",
          "message": "Update conversion documentation",
          "timestamp": "2022-08-10T21:53:23+02:00",
          "tree_id": "651a1502b01ca1f0a229dc5c7b7899799228d0cf",
          "url": "https://github.com/PyEllips/pyElli/commit/76bfacda6fd2bf4caaac3de53042366a98d0f951"
        },
        "date": 1660161294035,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 25.083592199768606,
            "unit": "iter/sec",
            "range": "stddev: 0.0008103144819335016",
            "extra": "mean: 39.86669819999804 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 6.639840529037762,
            "unit": "iter/sec",
            "range": "stddev: 0.024216912364622308",
            "extra": "mean: 150.60602669999952 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 133.96936988632143,
            "unit": "iter/sec",
            "range": "stddev: 0.001570188057112481",
            "extra": "mean: 7.4643928000000415 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 189.1130742434965,
            "unit": "iter/sec",
            "range": "stddev: 0.00017300486755206216",
            "extra": "mean: 5.287841700000229 msec\nrounds: 10"
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
          "id": "1c6daa716cca7458de414cb84545387e0fc80256",
          "message": "Add properties for absolute reflectance and transmittance for unpolarized light",
          "timestamp": "2022-08-11T11:54:06+02:00",
          "tree_id": "73af6a07cdea670af2b546fa3834c75c6529d44b",
          "url": "https://github.com/PyEllips/pyElli/commit/1c6daa716cca7458de414cb84545387e0fc80256"
        },
        "date": 1660211734401,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 24.106234536377467,
            "unit": "iter/sec",
            "range": "stddev: 0.0006977564540300522",
            "extra": "mean: 41.48304450000069 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 7.219862113875071,
            "unit": "iter/sec",
            "range": "stddev: 0.02669518470018045",
            "extra": "mean: 138.5068002999958 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 138.98566151645156,
            "unit": "iter/sec",
            "range": "stddev: 0.0015485776599249638",
            "extra": "mean: 7.194986799999015 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 193.38455793729972,
            "unit": "iter/sec",
            "range": "stddev: 0.00006128338651207747",
            "extra": "mean: 5.171043700005384 msec\nrounds: 10"
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
          "id": "53fc64090a175501b8f06b7260f3bc9f9574bd0a",
          "message": "Fix calculation error in MaxwellGarnettEMA",
          "timestamp": "2022-08-12T14:36:46+02:00",
          "tree_id": "9d49564d9751c8a0ea6ec3ac3130c18bbb5c02d0",
          "url": "https://github.com/PyEllips/pyElli/commit/53fc64090a175501b8f06b7260f3bc9f9574bd0a"
        },
        "date": 1660307883263,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 26.706562995778004,
            "unit": "iter/sec",
            "range": "stddev: 0.001050001153978191",
            "extra": "mean: 37.44397959999901 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 7.304326901159201,
            "unit": "iter/sec",
            "range": "stddev: 0.02164762562495744",
            "extra": "mean: 136.9051541000033 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 96.35775584249892,
            "unit": "iter/sec",
            "range": "stddev: 0.0032717233508445997",
            "extra": "mean: 10.377991800001496 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 200.84207458276032,
            "unit": "iter/sec",
            "range": "stddev: 0.00014596727055433037",
            "extra": "mean: 4.979036400004588 msec\nrounds: 10"
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
          "id": "0d8eea222e5ff8571738defa1895fb9357b20a8d",
          "message": "Prepare version 0.12.0",
          "timestamp": "2022-08-15T08:56:25+02:00",
          "tree_id": "017e7080be60e8fb6feecf74466b90c7d468c791",
          "url": "https://github.com/PyEllips/pyElli/commit/0d8eea222e5ff8571738defa1895fb9357b20a8d"
        },
        "date": 1660546660224,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 25.074849868665712,
            "unit": "iter/sec",
            "range": "stddev: 0.000831880835844661",
            "extra": "mean: 39.880597699993814 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 7.038451825289329,
            "unit": "iter/sec",
            "range": "stddev: 0.01855468476895071",
            "extra": "mean: 142.07669880000822 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 137.06945746672284,
            "unit": "iter/sec",
            "range": "stddev: 0.0014209054953506063",
            "extra": "mean: 7.295571299994208 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 172.19051247845448,
            "unit": "iter/sec",
            "range": "stddev: 0.0015377203558619445",
            "extra": "mean: 5.807520899998053 msec\nrounds: 10"
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
          "id": "0585a1ad7f4bf1ebbbbc0975983f8394e1308018",
          "message": "Move math.py into utils and import reorder\n\nFixes #78",
          "timestamp": "2022-08-15T10:34:27+02:00",
          "tree_id": "4684f02d697c49bd8c56306e321c1c18ecd87134",
          "url": "https://github.com/PyEllips/pyElli/commit/0585a1ad7f4bf1ebbbbc0975983f8394e1308018"
        },
        "date": 1660552571960,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 18.70613299575704,
            "unit": "iter/sec",
            "range": "stddev: 0.0016535903350974866",
            "extra": "mean: 53.45840319999979 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 4.186243515858339,
            "unit": "iter/sec",
            "range": "stddev: 0.02593489815973586",
            "extra": "mean: 238.87764680000032 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 71.01461254192483,
            "unit": "iter/sec",
            "range": "stddev: 0.006247213010359229",
            "extra": "mean: 14.08160889999408 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 128.92612109085667,
            "unit": "iter/sec",
            "range": "stddev: 0.0006615942560660066",
            "extra": "mean: 7.7563801000053445 msec\nrounds: 10"
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
          "id": "12af345b643664931e180dd57c203fed79feb268",
          "message": "Fix math docs",
          "timestamp": "2022-08-17T23:12:10+02:00",
          "tree_id": "fe25f520906cf67a740aa2dbe1684b810bda338b",
          "url": "https://github.com/PyEllips/pyElli/commit/12af345b643664931e180dd57c203fed79feb268"
        },
        "date": 1660770806086,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 23.859195985607503,
            "unit": "iter/sec",
            "range": "stddev: 0.0005924996933901868",
            "extra": "mean: 41.91256070000122 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 7.721748497842936,
            "unit": "iter/sec",
            "range": "stddev: 0.02238195553807543",
            "extra": "mean: 129.50434739998968 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 93.26704458959321,
            "unit": "iter/sec",
            "range": "stddev: 0.003258769410007335",
            "extra": "mean: 10.721900800012918 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 190.92546901647236,
            "unit": "iter/sec",
            "range": "stddev: 0.0002496715565950639",
            "extra": "mean: 5.237645900001553 msec\nrounds: 10"
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
          "id": "52da677d52db90cdb0d51970c3b4d469c78c436d",
          "message": "Fix bug in eigenvalue sorting (fixes #31)",
          "timestamp": "2022-08-19T12:24:23+02:00",
          "tree_id": "1ff56b9a199a64e68c060b96c8f2d58e6121686d",
          "url": "https://github.com/PyEllips/pyElli/commit/52da677d52db90cdb0d51970c3b4d469c78c436d"
        },
        "date": 1660904746860,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 24.86935332876999,
            "unit": "iter/sec",
            "range": "stddev: 0.0012068007995066962",
            "extra": "mean: 40.210132800001475 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 6.701545431731435,
            "unit": "iter/sec",
            "range": "stddev: 0.022214696293887934",
            "extra": "mean: 149.2193121999975 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 90.43439174334381,
            "unit": "iter/sec",
            "range": "stddev: 0.003397663080056956",
            "extra": "mean: 11.05774010000573 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 190.84669479666903,
            "unit": "iter/sec",
            "range": "stddev: 0.00008432452990152255",
            "extra": "mean: 5.239807800001017 msec\nrounds: 10"
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
          "id": "95f922e0cc0be6f24e11adfc010b77dacabd854f",
          "message": "Try to fix nbmake",
          "timestamp": "2022-08-22T09:35:32+02:00",
          "tree_id": "8cbaa43b69c6003186be6fa08852ea2f12c9310e",
          "url": "https://github.com/PyEllips/pyElli/commit/95f922e0cc0be6f24e11adfc010b77dacabd854f"
        },
        "date": 1661153812070,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 24.878939948970842,
            "unit": "iter/sec",
            "range": "stddev: 0.0015149043942833669",
            "extra": "mean: 40.19463860000059 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 5.790581569972305,
            "unit": "iter/sec",
            "range": "stddev: 0.01772782923220996",
            "extra": "mean: 172.6942256000001 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 127.38736339260976,
            "unit": "iter/sec",
            "range": "stddev: 0.0014436297782847544",
            "extra": "mean: 7.850072200002955 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 170.67283309890675,
            "unit": "iter/sec",
            "range": "stddev: 0.00011293104284393633",
            "extra": "mean: 5.859163299999182 msec\nrounds: 10"
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
          "id": "0570b27494c156b13d09158954b6987a9fb0196a",
          "message": "Revert \"Try to fix nbmake\"\n\nThis reverts commit 95f922e0cc0be6f24e11adfc010b77dacabd854f.",
          "timestamp": "2022-08-22T09:44:28+02:00",
          "tree_id": "1ff56b9a199a64e68c060b96c8f2d58e6121686d",
          "url": "https://github.com/PyEllips/pyElli/commit/0570b27494c156b13d09158954b6987a9fb0196a"
        },
        "date": 1661154352227,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 18.35931834142159,
            "unit": "iter/sec",
            "range": "stddev: 0.0014569840304018752",
            "extra": "mean: 54.46825320000244 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 3.8710485144845452,
            "unit": "iter/sec",
            "range": "stddev: 0.030148374308351922",
            "extra": "mean: 258.32794300000046 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 67.34777764018202,
            "unit": "iter/sec",
            "range": "stddev: 0.005338522091899218",
            "extra": "mean: 14.848299900000939 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 122.74896202255071,
            "unit": "iter/sec",
            "range": "stddev: 0.0004641966017726721",
            "extra": "mean: 8.146708399996783 msec\nrounds: 10"
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
          "id": "a4b486ca26b6e2298b07134fdfe89b9e3da9a3f8",
          "message": "Pin ipywidgets at version 7 to keep compatibility with plotly\n\nfixes #80",
          "timestamp": "2022-08-22T10:06:16+02:00",
          "tree_id": "148da071735ae2663fcbe9df7c888272b65953ee",
          "url": "https://github.com/PyEllips/pyElli/commit/a4b486ca26b6e2298b07134fdfe89b9e3da9a3f8"
        },
        "date": 1661155656419,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 24.185451293048036,
            "unit": "iter/sec",
            "range": "stddev: 0.0006252790086334531",
            "extra": "mean: 41.34717139999964 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 7.992462589866062,
            "unit": "iter/sec",
            "range": "stddev: 0.022081184525785943",
            "extra": "mean: 125.11788310000185 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 139.38013805713678,
            "unit": "iter/sec",
            "range": "stddev: 0.001346407718148331",
            "extra": "mean: 7.174623400000257 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 193.79262081111773,
            "unit": "iter/sec",
            "range": "stddev: 0.00009078579781092028",
            "extra": "mean: 5.160155199999394 msec\nrounds: 10"
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
          "id": "dba5cc651b557733483b2625aafe605bb0af3544",
          "message": "Prepare version 0.13.0",
          "timestamp": "2022-08-22T12:44:31+02:00",
          "tree_id": "a5628d21ecaeed6ba84d357288db72feb301e32c",
          "url": "https://github.com/PyEllips/pyElli/commit/dba5cc651b557733483b2625aafe605bb0af3544"
        },
        "date": 1661165151868,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 25.25250841752273,
            "unit": "iter/sec",
            "range": "stddev: 0.001030419776438861",
            "extra": "mean: 39.60002639999516 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 7.033328751963459,
            "unit": "iter/sec",
            "range": "stddev: 0.021003690893517807",
            "extra": "mean: 142.1801874000039 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 134.54692325972763,
            "unit": "iter/sec",
            "range": "stddev: 0.0012414948305291974",
            "extra": "mean: 7.432351299996753 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 176.59054931231066,
            "unit": "iter/sec",
            "range": "stddev: 0.0012790703033872233",
            "extra": "mean: 5.662817199981873 msec\nrounds: 10"
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
          "id": "d36864041059d295592352915d3a8679f5abedbb",
          "message": "Allow different separators during spectraray imports",
          "timestamp": "2022-08-23T12:05:13+02:00",
          "tree_id": "967ba000d298a91ed0ec27e4bdb5019e3a665bc2",
          "url": "https://github.com/PyEllips/pyElli/commit/d36864041059d295592352915d3a8679f5abedbb"
        },
        "date": 1661249198343,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 24.082639693704103,
            "unit": "iter/sec",
            "range": "stddev: 0.000716609183301981",
            "extra": "mean: 41.52368730000262 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 7.863363892894846,
            "unit": "iter/sec",
            "range": "stddev: 0.01938466027542292",
            "extra": "mean: 127.17203649999931 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 140.93379916650065,
            "unit": "iter/sec",
            "range": "stddev: 0.0012172178092114615",
            "extra": "mean: 7.095530000000849 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 176.7172168621102,
            "unit": "iter/sec",
            "range": "stddev: 0.0015743231014109492",
            "extra": "mean: 5.658758200002012 msec\nrounds: 10"
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
          "id": "958e594b12326559032deda5d3cd9c66a91c5fda",
          "message": "Docs: Bragg-mirror and cholesteric lq example",
          "timestamp": "2022-08-23T12:11:08+02:00",
          "tree_id": "abd3542d983fe06a74f9d482ce85224c40fc6d04",
          "url": "https://github.com/PyEllips/pyElli/commit/958e594b12326559032deda5d3cd9c66a91c5fda"
        },
        "date": 1661249553161,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 25.569158342108892,
            "unit": "iter/sec",
            "range": "stddev: 0.0007968094313663411",
            "extra": "mean: 39.109617400004026 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 6.244589504218851,
            "unit": "iter/sec",
            "range": "stddev: 0.023791186239313512",
            "extra": "mean: 160.13862869999684 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 90.99143484879237,
            "unit": "iter/sec",
            "range": "stddev: 0.0032633783010392737",
            "extra": "mean: 10.99004540000692 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 191.21219352488515,
            "unit": "iter/sec",
            "range": "stddev: 0.00011363761567567618",
            "extra": "mean: 5.229792000005773 msec\nrounds: 10"
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
          "id": "582fe24632e52488bbe1fb0b258d9450864015e2",
          "message": "Update plot_bragg_mirror.py",
          "timestamp": "2022-08-23T12:16:13+02:00",
          "tree_id": "090d42bea36dc8beecbe5023769665f8b79ecda8",
          "url": "https://github.com/PyEllips/pyElli/commit/582fe24632e52488bbe1fb0b258d9450864015e2"
        },
        "date": 1661249872731,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 21.29000187767106,
            "unit": "iter/sec",
            "range": "stddev: 0.0007886966266411464",
            "extra": "mean: 46.97040450000145 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 5.070918540180501,
            "unit": "iter/sec",
            "range": "stddev: 0.022726448559685506",
            "extra": "mean: 197.2029311999961 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 108.0017188257986,
            "unit": "iter/sec",
            "range": "stddev: 0.0018829343886485018",
            "extra": "mean: 9.259111899996242 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 121.66685883944584,
            "unit": "iter/sec",
            "range": "stddev: 0.0037842067240539882",
            "extra": "mean: 8.219165100001646 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "committer": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "distinct": true,
          "id": "04d13c4029470a9ca9539fd5757b6de27a48b421",
          "message": "Adds docs for fitting and plotting",
          "timestamp": "2022-08-23T20:27:25+02:00",
          "tree_id": "f8cb1b2da052c333a848cd745d25abac5ea08ca5",
          "url": "https://github.com/PyEllips/pyElli/commit/04d13c4029470a9ca9539fd5757b6de27a48b421"
        },
        "date": 1661279331033,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 25.57899794833286,
            "unit": "iter/sec",
            "range": "stddev: 0.0012890637995262289",
            "extra": "mean: 39.09457289999807 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 5.745957048663199,
            "unit": "iter/sec",
            "range": "stddev: 0.013892004656374524",
            "extra": "mean: 174.03541159999634 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 90.63912064027022,
            "unit": "iter/sec",
            "range": "stddev: 0.00338289610401857",
            "extra": "mean: 11.03276370000117 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 193.33183797610934,
            "unit": "iter/sec",
            "range": "stddev: 0.00006736400823909231",
            "extra": "mean: 5.172453799997356 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "committer": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "distinct": true,
          "id": "53399f5e2d40a4677440c3edf828bdaf1839280f",
          "message": "Sphinx linting",
          "timestamp": "2022-08-23T20:29:09+02:00",
          "tree_id": "632a5f05780397cc5537be1d65c5c3f1d78ada0a",
          "url": "https://github.com/PyEllips/pyElli/commit/53399f5e2d40a4677440c3edf828bdaf1839280f"
        },
        "date": 1661279460801,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 19.932384567775294,
            "unit": "iter/sec",
            "range": "stddev: 0.0003132931611607977",
            "extra": "mean: 50.16961199999628 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 5.438783771167006,
            "unit": "iter/sec",
            "range": "stddev: 0.04577150393862326",
            "extra": "mean: 183.86463630000662 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 88.66677428446228,
            "unit": "iter/sec",
            "range": "stddev: 0.004114373243536056",
            "extra": "mean: 11.27818180000304 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 154.87642278550103,
            "unit": "iter/sec",
            "range": "stddev: 0.00014731088877960774",
            "extra": "mean: 6.456760700012865 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "committer": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "distinct": true,
          "id": "6d86168d932091a3445b2d0311decd5b3fb352e9",
          "message": "Accept a single dataframe and a list in plot_mmatrix",
          "timestamp": "2022-08-25T18:27:52+02:00",
          "tree_id": "7b68b2530a8c1d0810a4abec8669d750cc2c3754",
          "url": "https://github.com/PyEllips/pyElli/commit/6d86168d932091a3445b2d0311decd5b3fb352e9"
        },
        "date": 1661444947738,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 25.045544445978454,
            "unit": "iter/sec",
            "range": "stddev: 0.0027707367031758645",
            "extra": "mean: 39.927261400004 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 6.375264256217184,
            "unit": "iter/sec",
            "range": "stddev: 0.0180126176658251",
            "extra": "mean: 156.8562431000089 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 137.18546271459243,
            "unit": "iter/sec",
            "range": "stddev: 0.0013815844760666956",
            "extra": "mean: 7.289402099991094 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 192.10564519548126,
            "unit": "iter/sec",
            "range": "stddev: 0.00008048722037359569",
            "extra": "mean: 5.205469099996662 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "committer": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "distinct": true,
          "id": "50b5749d587fdb5e32a7b0eb5231b6871df9ae23",
          "message": "Moves requirements files and fixes benchmark action",
          "timestamp": "2022-09-06T21:16:21+02:00",
          "tree_id": "41325e160a85cc2e7bb072905ac1712eab9a0781",
          "url": "https://github.com/PyEllips/pyElli/commit/50b5749d587fdb5e32a7b0eb5231b6871df9ae23"
        },
        "date": 1662491857507,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 24.156261288671534,
            "unit": "iter/sec",
            "range": "stddev: 0.0012233097566777835",
            "extra": "mean: 41.39713460000394 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 7.96086421954169,
            "unit": "iter/sec",
            "range": "stddev: 0.0191950148262367",
            "extra": "mean: 125.6145027000059 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 94.42234463250442,
            "unit": "iter/sec",
            "range": "stddev: 0.002763356986271815",
            "extra": "mean: 10.59071349998817 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 188.29105662493944,
            "unit": "iter/sec",
            "range": "stddev: 0.000574018520045964",
            "extra": "mean: 5.310926699996799 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "committer": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "distinct": true,
          "id": "9ccdcb8009c4b2892e17f8448e12828460cb8290",
          "message": "Corrects testing and benchmarking action",
          "timestamp": "2022-09-07T11:15:14+02:00",
          "tree_id": "63f89a357b25552954a7014af97272865e7f40ac",
          "url": "https://github.com/PyEllips/pyElli/commit/9ccdcb8009c4b2892e17f8448e12828460cb8290"
        },
        "date": 1662542194717,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 21.49047521829416,
            "unit": "iter/sec",
            "range": "stddev: 0.0013130523329050563",
            "extra": "mean: 46.532242300008875 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 5.584757489216711,
            "unit": "iter/sec",
            "range": "stddev: 0.01635785247084898",
            "extra": "mean: 179.05880459999253 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 114.14088580746406,
            "unit": "iter/sec",
            "range": "stddev: 0.0017165180283862445",
            "extra": "mean: 8.761102500000106 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 146.7285203678509,
            "unit": "iter/sec",
            "range": "stddev: 0.0017434931902693344",
            "extra": "mean: 6.815307600001574 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "committer": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "distinct": true,
          "id": "141546d805d7b08f9d11cf3f86557075221501fb",
          "message": "Updates to use hashes in requirements files",
          "timestamp": "2022-09-10T08:44:20+02:00",
          "tree_id": "fc4998c2f34b1a5681d31145f8ca6c286a95734e",
          "url": "https://github.com/PyEllips/pyElli/commit/141546d805d7b08f9d11cf3f86557075221501fb"
        },
        "date": 1662792332107,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 24.424113237263082,
            "unit": "iter/sec",
            "range": "stddev: 0.0009311086817035394",
            "extra": "mean: 40.943144599998504 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 7.435634994588532,
            "unit": "iter/sec",
            "range": "stddev: 0.027998547047644703",
            "extra": "mean: 134.48750519999635 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 149.28527287051767,
            "unit": "iter/sec",
            "range": "stddev: 0.00011336411620247532",
            "extra": "mean: 6.698584399998708 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 194.1350255698096,
            "unit": "iter/sec",
            "range": "stddev: 0.00010398527963334412",
            "extra": "mean: 5.151053999992428 msec\nrounds: 10"
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
          "id": "c7ad80b198510456234dc7639e306c5989499bae",
          "message": "Include Logo\n\nfixes #66",
          "timestamp": "2022-09-13T11:04:58+02:00",
          "tree_id": "8560f621c7719347f3a2410909633aa03cd6f26a",
          "url": "https://github.com/PyEllips/pyElli/commit/c7ad80b198510456234dc7639e306c5989499bae"
        },
        "date": 1663059977240,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 25.131116637662902,
            "unit": "iter/sec",
            "range": "stddev: 0.0009416639426691965",
            "extra": "mean: 39.79130789999772 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 7.2004567699037985,
            "unit": "iter/sec",
            "range": "stddev: 0.020047268501528933",
            "extra": "mean: 138.88007829999935 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 142.97513410778214,
            "unit": "iter/sec",
            "range": "stddev: 0.00015477887104251527",
            "extra": "mean: 6.99422320000167 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 186.5269669215778,
            "unit": "iter/sec",
            "range": "stddev: 0.00008080288468817674",
            "extra": "mean: 5.3611551000045665 msec\nrounds: 10"
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
          "id": "ca1d30f529b08f5bdf527a00c4735219243b579f",
          "message": "Add dark-mode logo",
          "timestamp": "2022-09-13T11:10:16+02:00",
          "tree_id": "a2c9f2ece2c1469e40ee0e01638070d92e2cd76d",
          "url": "https://github.com/PyEllips/pyElli/commit/ca1d30f529b08f5bdf527a00c4735219243b579f"
        },
        "date": 1663060313906,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 19.900354507105007,
            "unit": "iter/sec",
            "range": "stddev: 0.0012529248698811414",
            "extra": "mean: 50.25036109999803 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 4.299273035750367,
            "unit": "iter/sec",
            "range": "stddev: 0.022623873752599517",
            "extra": "mean: 232.59746280000257 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 102.00351738728531,
            "unit": "iter/sec",
            "range": "stddev: 0.002492696244169674",
            "extra": "mean: 9.803583500000457 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 137.51534929139092,
            "unit": "iter/sec",
            "range": "stddev: 0.00024662263625189703",
            "extra": "mean: 7.271915500000148 msec\nrounds: 10"
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
          "id": "5de93798014bfc7b63335f5eb616f452dc2b0cea",
          "message": "Change result index conversion to use 1...4",
          "timestamp": "2022-09-13T15:59:33+02:00",
          "tree_id": "d4141bdb3a9ebf91dd2aa875c564f665763d9128",
          "url": "https://github.com/PyEllips/pyElli/commit/5de93798014bfc7b63335f5eb616f452dc2b0cea"
        },
        "date": 1663077646777,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 24.25529048331484,
            "unit": "iter/sec",
            "range": "stddev: 0.000668224388910675",
            "extra": "mean: 41.228118899994115 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 6.603882795682732,
            "unit": "iter/sec",
            "range": "stddev: 0.019342425266716354",
            "extra": "mean: 151.42606720000344 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 93.98816895729416,
            "unit": "iter/sec",
            "range": "stddev: 0.0032410670512264287",
            "extra": "mean: 10.639636999997037 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 186.82688840991236,
            "unit": "iter/sec",
            "range": "stddev: 0.0001760193494357481",
            "extra": "mean: 5.3525485999955436 msec\nrounds: 10"
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
          "id": "9c9cbc458300710e758ecdf6239f5c677f0e26b4",
          "message": "Fix linting",
          "timestamp": "2022-09-13T16:25:50+02:00",
          "tree_id": "1ce2e776c04b775a549861a4d3184e0968568983",
          "url": "https://github.com/PyEllips/pyElli/commit/9c9cbc458300710e758ecdf6239f5c677f0e26b4"
        },
        "date": 1663079224514,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 25.305477475363357,
            "unit": "iter/sec",
            "range": "stddev: 0.0009296517821278754",
            "extra": "mean: 39.517136200001346 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 6.539961688708239,
            "unit": "iter/sec",
            "range": "stddev: 0.023887515289047975",
            "extra": "mean: 152.90609449999977 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 90.73242415630344,
            "unit": "iter/sec",
            "range": "stddev: 0.0034499136452574267",
            "extra": "mean: 11.021418300003916 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 179.177737237967,
            "unit": "iter/sec",
            "range": "stddev: 0.0002811534752449375",
            "extra": "mean: 5.581050499995399 msec\nrounds: 10"
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
          "id": "150a7b959a9d0274327458afdcdd52bef0e7811b",
          "message": "Merge pull request #86 from PyEllips/restructure-dispersions\n\nRestructure dispersions and importers",
          "timestamp": "2022-09-15T11:23:40+02:00",
          "tree_id": "03f10307f263509976ccaf66a4ec5bf900e8db7b",
          "url": "https://github.com/PyEllips/pyElli/commit/150a7b959a9d0274327458afdcdd52bef0e7811b"
        },
        "date": 1663233910549,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 17.07313688109078,
            "unit": "iter/sec",
            "range": "stddev: 0.003170973249817378",
            "extra": "mean: 58.57154469999841 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 4.08883646193685,
            "unit": "iter/sec",
            "range": "stddev: 0.028337337824953054",
            "extra": "mean: 244.56835319999755 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 91.83585157032013,
            "unit": "iter/sec",
            "range": "stddev: 0.0025794493452563493",
            "extra": "mean: 10.88899360000255 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 130.80066106129144,
            "unit": "iter/sec",
            "range": "stddev: 0.00017503246873352586",
            "extra": "mean: 7.645221300001026 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "committer": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "distinct": true,
          "id": "a29f64271d468a0a3c5fee8077fdbe544950783a",
          "message": "Uses correct extra requirement in dockerfile",
          "timestamp": "2022-09-16T17:34:31+02:00",
          "tree_id": "2b04a7d180eee5594b4dc50070dd162ed5e55d69",
          "url": "https://github.com/PyEllips/pyElli/commit/a29f64271d468a0a3c5fee8077fdbe544950783a"
        },
        "date": 1663342550420,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 25.529231695320757,
            "unit": "iter/sec",
            "range": "stddev: 0.0009594642045596704",
            "extra": "mean: 39.17078320000087 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 5.921291135732074,
            "unit": "iter/sec",
            "range": "stddev: 0.015295888134032284",
            "extra": "mean: 168.8820862 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 88.1376521158729,
            "unit": "iter/sec",
            "range": "stddev: 0.003512608356600843",
            "extra": "mean: 11.345888800002513 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 190.2460073025082,
            "unit": "iter/sec",
            "range": "stddev: 0.00013408934059044864",
            "extra": "mean: 5.256352099993933 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "github@schroedingerscat.org",
            "name": "Florian Dobener",
            "username": "domna"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "3d2bc42058871e806efcdae8c404e7ea8129b407",
          "message": "Kramers-Kronig relations (#89)\n\n* Adds kkrs\r\n\r\n* Adds kkr tests\r\n\r\n* Adds energy formulation of kkr's\r\n\r\n* Fixes kkr tests\r\n\r\n* Adds cody lorentz dispersion model\r\n\r\n* Adds test for energy form of kkr\r\n\r\n* Corrects typos in cody-lorentz docs\r\n\r\n* Adds docs for kkrs",
          "timestamp": "2022-11-08T07:39:36+01:00",
          "tree_id": "ca25896ccb4d2e811ac5b46e2b1a0e0fce4c6901",
          "url": "https://github.com/PyEllips/pyElli/commit/3d2bc42058871e806efcdae8c404e7ea8129b407"
        },
        "date": 1667889648008,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 30.097214333370403,
            "unit": "iter/sec",
            "range": "stddev: 0.0018298823647963853",
            "extra": "mean: 33.22566629999528 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 6.263486244982048,
            "unit": "iter/sec",
            "range": "stddev: 0.016468109380258993",
            "extra": "mean: 159.6554954999931 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 167.8984057489475,
            "unit": "iter/sec",
            "range": "stddev: 0.00004867148748944657",
            "extra": "mean: 5.955982700010054 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 203.00784956269223,
            "unit": "iter/sec",
            "range": "stddev: 0.00006463426285876842",
            "extra": "mean: 4.925917899993237 msec\nrounds: 10"
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
          "id": "fb8dd83fae9ddfe6fc4fde83d26023a5f65fe5e8",
          "message": "Merge pull request #87 from PyEllips/rii-importer\n\nInclude refractiveindex.info database and utilities to read dispersions.",
          "timestamp": "2022-11-08T18:13:18+01:00",
          "tree_id": "396097f51dae6c88f924c3939bb4adc93781768a",
          "url": "https://github.com/PyEllips/pyElli/commit/fb8dd83fae9ddfe6fc4fde83d26023a5f65fe5e8"
        },
        "date": 1667927692091,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 24.672770047101807,
            "unit": "iter/sec",
            "range": "stddev: 0.0020711676045683234",
            "extra": "mean: 40.530511899999055 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 6.312554595114948,
            "unit": "iter/sec",
            "range": "stddev: 0.024309928612012793",
            "extra": "mean: 158.4144714999951 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 84.8882987982904,
            "unit": "iter/sec",
            "range": "stddev: 0.004033722692551262",
            "extra": "mean: 11.78018659999509 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 167.71782134030548,
            "unit": "iter/sec",
            "range": "stddev: 0.0001524239124124416",
            "extra": "mean: 5.962395599993897 msec\nrounds: 10"
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
          "id": "efbc94edcad957db169678b670d100059c7c6656",
          "message": "Reenable Python 3.7",
          "timestamp": "2022-11-08T19:33:21+01:00",
          "tree_id": "f78c7b77e90504081ea0cfdeb063b1e19c507ba2",
          "url": "https://github.com/PyEllips/pyElli/commit/efbc94edcad957db169678b670d100059c7c6656"
        },
        "date": 1667932512517,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 17.583385062773065,
            "unit": "iter/sec",
            "range": "stddev: 0.0017639956866519885",
            "extra": "mean: 56.87187059999985 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 3.805675144023608,
            "unit": "iter/sec",
            "range": "stddev: 0.036676732353645526",
            "extra": "mean: 262.7654652999979 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 73.65878041386395,
            "unit": "iter/sec",
            "range": "stddev: 0.004362703792380477",
            "extra": "mean: 13.576114000005646 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 117.86828650376326,
            "unit": "iter/sec",
            "range": "stddev: 0.0011018570016586879",
            "extra": "mean: 8.484046300003456 msec\nrounds: 10"
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
          "id": "89cbc3c1f612a2c898eba0ea20b898267e5f5fe3",
          "message": "Benchmark with Python 3.10",
          "timestamp": "2022-11-09T08:37:11+01:00",
          "tree_id": "f4f0691f6dfdf1a9f08034c86a62accd8a7dd19b",
          "url": "https://github.com/PyEllips/pyElli/commit/89cbc3c1f612a2c898eba0ea20b898267e5f5fe3"
        },
        "date": 1667979527560,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 24.473179328835833,
            "unit": "iter/sec",
            "range": "stddev: 0.0007687087734143662",
            "extra": "mean: 40.86105800000155 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 6.349327683850933,
            "unit": "iter/sec",
            "range": "stddev: 0.02230753103028657",
            "extra": "mean: 157.4969901999907 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 150.10420158634733,
            "unit": "iter/sec",
            "range": "stddev: 0.00009511917078162511",
            "extra": "mean: 6.662038699994355 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 192.84634180856716,
            "unit": "iter/sec",
            "range": "stddev: 0.00030237773316088226",
            "extra": "mean: 5.1854756000125235 msec\nrounds: 10"
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
          "id": "e311b242a33fb053ef9fe8115b025c9dd46d23c3",
          "message": "Fix typos in docs",
          "timestamp": "2022-11-09T09:01:45+01:00",
          "tree_id": "6dd65d2d64c06f922501eaf89f22f44a50bed728",
          "url": "https://github.com/PyEllips/pyElli/commit/e311b242a33fb053ef9fe8115b025c9dd46d23c3"
        },
        "date": 1667981014464,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 20.17172382137632,
            "unit": "iter/sec",
            "range": "stddev: 0.0016766666400641747",
            "extra": "mean: 49.574345200001346 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 4.022521606115996,
            "unit": "iter/sec",
            "range": "stddev: 0.020518539864623205",
            "extra": "mean: 248.6002806000002 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 96.82005939678442,
            "unit": "iter/sec",
            "range": "stddev: 0.002025495548114163",
            "extra": "mean: 10.328438199999823 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 128.69683426004096,
            "unit": "iter/sec",
            "range": "stddev: 0.00031357317557362366",
            "extra": "mean: 7.770198899993375 msec\nrounds: 10"
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
          "id": "2da5fb534bc423378bf4bda7a0bf413e871f737e",
          "message": "Include RII in documentation and readme",
          "timestamp": "2022-11-12T08:59:55+01:00",
          "tree_id": "99f84b0e3b6f1b69c9d17a5dd14d86c902bedcfe",
          "url": "https://github.com/PyEllips/pyElli/commit/2da5fb534bc423378bf4bda7a0bf413e871f737e"
        },
        "date": 1668240080486,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 25.389634794326504,
            "unit": "iter/sec",
            "range": "stddev: 0.0010454277761158366",
            "extra": "mean: 39.38615139999797 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 5.317525176116724,
            "unit": "iter/sec",
            "range": "stddev: 0.048585841853087286",
            "extra": "mean: 188.05740770000057 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 89.8647667361598,
            "unit": "iter/sec",
            "range": "stddev: 0.003560995480590978",
            "extra": "mean: 11.127831700002844 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 188.53740823517592,
            "unit": "iter/sec",
            "range": "stddev: 0.00040654820513924143",
            "extra": "mean: 5.303987199997096 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "committer": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "distinct": true,
          "id": "473696338318a796c8fcfbf4707a3cfc202b8219",
          "message": "Updates examples to use rii database",
          "timestamp": "2022-11-13T08:11:06+01:00",
          "tree_id": "ec152574b852ff49568e420c5eb18adc3ed692f6",
          "url": "https://github.com/PyEllips/pyElli/commit/473696338318a796c8fcfbf4707a3cfc202b8219"
        },
        "date": 1668323575081,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 18.093872388705986,
            "unit": "iter/sec",
            "range": "stddev: 0.006953870988334632",
            "extra": "mean: 55.267329099999074 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 3.9567005251896754,
            "unit": "iter/sec",
            "range": "stddev: 0.03506061338652649",
            "extra": "mean: 252.73583220000262 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 92.96508734263607,
            "unit": "iter/sec",
            "range": "stddev: 0.0029805854670690657",
            "extra": "mean: 10.756726299996444 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 124.49638411457912,
            "unit": "iter/sec",
            "range": "stddev: 0.0006083057820688778",
            "extra": "mean: 8.032361799999421 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "committer": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "distinct": true,
          "id": "a161bbd8eb051d812c1f6668948c34f540f626dc",
          "message": "Adds submodule to rtd config",
          "timestamp": "2022-11-13T08:20:07+01:00",
          "tree_id": "57b9d1ecdb0062c9a808f7da4a17769877c9a6e9",
          "url": "https://github.com/PyEllips/pyElli/commit/a161bbd8eb051d812c1f6668948c34f540f626dc"
        },
        "date": 1668324118635,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 18.158506687120113,
            "unit": "iter/sec",
            "range": "stddev: 0.0009671958596599443",
            "extra": "mean: 55.070607799996196 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 3.6118369544937576,
            "unit": "iter/sec",
            "range": "stddev: 0.04047479059959127",
            "extra": "mean: 276.86742580000043 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 75.86591746035624,
            "unit": "iter/sec",
            "range": "stddev: 0.005639001582261062",
            "extra": "mean: 13.181149500005063 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 126.98500580098023,
            "unit": "iter/sec",
            "range": "stddev: 0.0005465009631352575",
            "extra": "mean: 7.874945500000763 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "committer": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "distinct": true,
          "id": "adbb431c335d0bf10c2b47f271bab6b2d7e1b004",
          "message": "Updates rri submodule",
          "timestamp": "2022-11-16T09:09:40+01:00",
          "tree_id": "dcf8f5f862a9301737af90573de5d8f2efdaab52",
          "url": "https://github.com/PyEllips/pyElli/commit/adbb431c335d0bf10c2b47f271bab6b2d7e1b004"
        },
        "date": 1668586294415,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 21.22038042853687,
            "unit": "iter/sec",
            "range": "stddev: 0.0015480059375161874",
            "extra": "mean: 47.12450860000672 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 4.74917263713651,
            "unit": "iter/sec",
            "range": "stddev: 0.02306706494838473",
            "extra": "mean: 210.56299200000126 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 72.13763595470418,
            "unit": "iter/sec",
            "range": "stddev: 0.003976704330475319",
            "extra": "mean: 13.862389400006236 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 153.27672374316094,
            "unit": "iter/sec",
            "range": "stddev: 0.000405922014539383",
            "extra": "mean: 6.524147799999014 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "49699333+dependabot[bot]@users.noreply.github.com",
            "name": "dependabot[bot]",
            "username": "dependabot[bot]"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "100cadd1300d29fbe107e4156985e8721ec5ffcf",
          "message": "Bump pillow from 9.2.0 to 9.3.0 in /requirements (#97)\n\n* Bump pillow from 9.2.0 to 9.3.0 in /requirements\r\n\r\nBumps [pillow](https://github.com/python-pillow/Pillow) from 9.2.0 to 9.3.0.\r\n- [Release notes](https://github.com/python-pillow/Pillow/releases)\r\n- [Changelog](https://github.com/python-pillow/Pillow/blob/main/CHANGES.rst)\r\n- [Commits](https://github.com/python-pillow/Pillow/compare/9.2.0...9.3.0)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: pillow\r\n  dependency-type: direct:production\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\n\r\n* Adds checking of requirements files\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>\r\nCo-authored-by: domna <florian.dobener@physik.hu-berlin.de>",
          "timestamp": "2022-11-16T10:07:06+01:00",
          "tree_id": "e97211261a2fa13608ec78d161bfa460aed23f0c",
          "url": "https://github.com/PyEllips/pyElli/commit/100cadd1300d29fbe107e4156985e8721ec5ffcf"
        },
        "date": 1668589731778,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 17.231908772123646,
            "unit": "iter/sec",
            "range": "stddev: 0.0036565713693811133",
            "extra": "mean: 58.0318764000026 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 3.731936200515938,
            "unit": "iter/sec",
            "range": "stddev: 0.020993813380755",
            "extra": "mean: 267.95742110000447 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 95.08260167909022,
            "unit": "iter/sec",
            "range": "stddev: 0.00032108707957430896",
            "extra": "mean: 10.5171711999958 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 117.14135545761702,
            "unit": "iter/sec",
            "range": "stddev: 0.0005615074833031281",
            "extra": "mean: 8.536694800000078 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "committer": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "distinct": true,
          "id": "a644842b91aee3d1c930d544a777d74f296c4522",
          "message": "Removes silicon material file from examples",
          "timestamp": "2022-11-16T19:33:25+01:00",
          "tree_id": "903f8a691894ff16a01b673f339c50333f5f9d02",
          "url": "https://github.com/PyEllips/pyElli/commit/a644842b91aee3d1c930d544a777d74f296c4522"
        },
        "date": 1668623693731,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 23.89169462863189,
            "unit": "iter/sec",
            "range": "stddev: 0.0019167384655567436",
            "extra": "mean: 41.855549199996744 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 6.169888981473314,
            "unit": "iter/sec",
            "range": "stddev: 0.021800445275360875",
            "extra": "mean: 162.07747059999917 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 146.56764302655017,
            "unit": "iter/sec",
            "range": "stddev: 0.00015372860293988604",
            "extra": "mean: 6.822788299999161 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 178.29915302911206,
            "unit": "iter/sec",
            "range": "stddev: 0.0004152344870504958",
            "extra": "mean: 5.6085515999996005 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "committer": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "distinct": true,
          "id": "bd9c0691c9ac682cf8eee025e6662c588406e4f5",
          "message": "Adds guard clause to only accept dispersions in dispersions add (fixes #99)",
          "timestamp": "2023-01-16T18:20:06+01:00",
          "tree_id": "941fa75c3cc8a53e300beef7b47a1e7cc0cb1fcd",
          "url": "https://github.com/PyEllips/pyElli/commit/bd9c0691c9ac682cf8eee025e6662c588406e4f5"
        },
        "date": 1673889697783,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 24.439251874617128,
            "unit": "iter/sec",
            "range": "stddev: 0.0007255026593549474",
            "extra": "mean: 40.91778279999687 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 5.9826806229969,
            "unit": "iter/sec",
            "range": "stddev: 0.027259219814736425",
            "extra": "mean: 167.1491532000033 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 95.6265759260011,
            "unit": "iter/sec",
            "range": "stddev: 0.0030459970561091563",
            "extra": "mean: 10.457343999996738 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 196.77648243967974,
            "unit": "iter/sec",
            "range": "stddev: 0.00007221296522289753",
            "extra": "mean: 5.081908100001442 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "github@schroedingerscat.org",
            "name": "Florian Dobener",
            "username": "domna"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "1ceb7b887dbf5afbf2b9085286b740e1d63e735e",
          "message": "Change built process to pyproject.toml (#104)\n\n* Update setup.cfg\r\n\r\n* Changes package method to pyproject.toml (fixes #103)\r\n\r\n* Corrects rii include path\r\n\r\n* Update actions to newer versions\r\n\r\n* Fix tests\r\n\r\nCo-authored-by: Marius Müller <49639740+MarJMue@users.noreply.github.com>",
          "timestamp": "2023-01-21T16:27:28+01:00",
          "tree_id": "182413aff6a84bd89b8bc2b5aa0b4b500a0354a1",
          "url": "https://github.com/PyEllips/pyElli/commit/1ceb7b887dbf5afbf2b9085286b740e1d63e735e"
        },
        "date": 1674314942648,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 22.41231049046639,
            "unit": "iter/sec",
            "range": "stddev: 0.0011127317133105587",
            "extra": "mean: 44.618336000002046 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 5.242060818163154,
            "unit": "iter/sec",
            "range": "stddev: 0.024869226271464068",
            "extra": "mean: 190.76466960000005 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 83.0543523794545,
            "unit": "iter/sec",
            "range": "stddev: 0.0041900155590991715",
            "extra": "mean: 12.040308199999572 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 159.70816080596862,
            "unit": "iter/sec",
            "range": "stddev: 0.0004899289665960167",
            "extra": "mean: 6.261420799998518 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "committer": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "distinct": true,
          "id": "a2cf6d27d0312c2519f4f509596d80adc8e04ee0",
          "message": "Updates generate ipynb script",
          "timestamp": "2023-01-21T16:32:55+01:00",
          "tree_id": "86fdda121fa215a081c9bae87a00454a81cd4bf7",
          "url": "https://github.com/PyEllips/pyElli/commit/a2cf6d27d0312c2519f4f509596d80adc8e04ee0"
        },
        "date": 1674315276502,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 24.3895184629792,
            "unit": "iter/sec",
            "range": "stddev: 0.0008470806606802803",
            "extra": "mean: 41.00121950000357 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 7.275387831790789,
            "unit": "iter/sec",
            "range": "stddev: 0.015172269286736862",
            "extra": "mean: 137.44971720000478 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 148.1665207966506,
            "unit": "iter/sec",
            "range": "stddev: 0.0002057170610342187",
            "extra": "mean: 6.7491630000034775 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 195.30906683281808,
            "unit": "iter/sec",
            "range": "stddev: 0.0002798332364047458",
            "extra": "mean: 5.120089999999777 msec\nrounds: 10"
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
          "id": "ec1b452b03964dd446c68a835b5a784d38a03dcf",
          "message": "Merge pull request #107 from PyEllips/update-requirements-process\n\nUpdates requirements generation and ci/cd",
          "timestamp": "2023-01-21T16:56:55+01:00",
          "tree_id": "83ae8cc18e061ce42f0ccfa6920cc0e3bd1f812f",
          "url": "https://github.com/PyEllips/pyElli/commit/ec1b452b03964dd446c68a835b5a784d38a03dcf"
        },
        "date": 1674316705028,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 23.772113860342156,
            "unit": "iter/sec",
            "range": "stddev: 0.0011972284881852843",
            "extra": "mean: 42.06609500000127 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 6.6978961791556735,
            "unit": "iter/sec",
            "range": "stddev: 0.02237964760780043",
            "extra": "mean: 149.30061220000255 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 94.44994373997515,
            "unit": "iter/sec",
            "range": "stddev: 0.0033932814817007246",
            "extra": "mean: 10.58761879999679 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 193.81708384795763,
            "unit": "iter/sec",
            "range": "stddev: 0.00008376022442836337",
            "extra": "mean: 5.159503899999152 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "49699333+dependabot[bot]@users.noreply.github.com",
            "name": "dependabot[bot]",
            "username": "dependabot[bot]"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "2c00bf9268a897a1bd34e26fd8077470b7633570",
          "message": "Bump future from 0.18.2 to 0.18.3 in /requirements (#106)\n\nBumps [future](https://github.com/PythonCharmers/python-future) from 0.18.2 to 0.18.3.\r\n- [Release notes](https://github.com/PythonCharmers/python-future/releases)\r\n- [Changelog](https://github.com/PythonCharmers/python-future/blob/master/docs/changelog.rst)\r\n- [Commits](https://github.com/PythonCharmers/python-future/compare/v0.18.2...v0.18.3)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: future\r\n  dependency-type: direct:production\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2023-01-22T00:04:13+01:00",
          "tree_id": "41385813cb96762b5a9acb2b127342d43df5720d",
          "url": "https://github.com/PyEllips/pyElli/commit/2c00bf9268a897a1bd34e26fd8077470b7633570"
        },
        "date": 1674342351615,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 22.624055564174522,
            "unit": "iter/sec",
            "range": "stddev: 0.002008694648868758",
            "extra": "mean: 44.20074009999837 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 5.219673026768041,
            "unit": "iter/sec",
            "range": "stddev: 0.020533958536451787",
            "extra": "mean: 191.58288170000333 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 123.00331183961566,
            "unit": "iter/sec",
            "range": "stddev: 0.001509186814271779",
            "extra": "mean: 8.129862399997023 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 124.65566055241948,
            "unit": "iter/sec",
            "range": "stddev: 0.0027522384199005208",
            "extra": "mean: 8.022098600002892 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "49699333+dependabot[bot]@users.noreply.github.com",
            "name": "dependabot[bot]",
            "username": "dependabot[bot]"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "373788f02004fe8d799c0e9f1a3be1b7b20c3055",
          "message": "Bump jupyter-core from 4.11.1 to 4.11.2 in /requirements (#105)\n\nBumps [jupyter-core](https://github.com/jupyter/jupyter_core) from 4.11.1 to 4.11.2.\r\n- [Release notes](https://github.com/jupyter/jupyter_core/releases)\r\n- [Changelog](https://github.com/jupyter/jupyter_core/blob/main/CHANGELOG.md)\r\n- [Commits](https://github.com/jupyter/jupyter_core/compare/4.11.1...4.11.2)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: jupyter-core\r\n  dependency-type: direct:production\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2023-01-22T00:04:28+01:00",
          "tree_id": "65cbc9059aef97f26017fcc80f02a04f422a21a4",
          "url": "https://github.com/PyEllips/pyElli/commit/373788f02004fe8d799c0e9f1a3be1b7b20c3055"
        },
        "date": 1674342357624,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 24.239907523005055,
            "unit": "iter/sec",
            "range": "stddev: 0.003238027701838348",
            "extra": "mean: 41.254282800004205 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 5.975530177630255,
            "unit": "iter/sec",
            "range": "stddev: 0.03379890835361012",
            "extra": "mean: 167.34916740000045 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 139.2557543054379,
            "unit": "iter/sec",
            "range": "stddev: 0.00022421626548790264",
            "extra": "mean: 7.181031799997584 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 182.19829383690129,
            "unit": "iter/sec",
            "range": "stddev: 0.00042652862312686014",
            "extra": "mean: 5.48852559999915 msec\nrounds: 10"
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
          "id": "7132704347474ca6ba0fe9028771895ed721dc7a",
          "message": "Merge pull request #111 from PyEllips/eps-inf-in-rii-reader\n\nChanges ConstantRefInd to EpsilonInf in rii reader",
          "timestamp": "2023-01-26T21:08:07+01:00",
          "tree_id": "313491a369c28673235145e627063e053bb6a292",
          "url": "https://github.com/PyEllips/pyElli/commit/7132704347474ca6ba0fe9028771895ed721dc7a"
        },
        "date": 1674763773709,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 24.509352060428217,
            "unit": "iter/sec",
            "range": "stddev: 0.0006061756656126372",
            "extra": "mean: 40.80075219999628 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 6.41787883032094,
            "unit": "iter/sec",
            "range": "stddev: 0.021149810973184083",
            "extra": "mean: 155.81472109999197 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 133.98849598877993,
            "unit": "iter/sec",
            "range": "stddev: 0.00097454876384148",
            "extra": "mean: 7.46332730000745 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 194.12561899869766,
            "unit": "iter/sec",
            "range": "stddev: 0.00022318188137447132",
            "extra": "mean: 5.151303599998869 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "github@schroedingerscat.org",
            "name": "Florian Dobener",
            "username": "domna"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "7dc8f174cf9644b0cedf3956a36c76ae8eade4ea",
          "message": "Python 3.11 compatibility (#90)\n\n* Updates actions with py3.11\r\n\r\n* Updates setup.cfg\r\n\r\n* Updates pyproject\r\n\r\n* Removes duplicate submodule\r\n\r\n* Tune setuptools version in pyproject to support pyproject installs (support pep660 and pep518)",
          "timestamp": "2023-01-27T11:15:39+01:00",
          "tree_id": "4ebd92ae8160bc4116d34bf8b9edd184a8b2d7e3",
          "url": "https://github.com/PyEllips/pyElli/commit/7dc8f174cf9644b0cedf3956a36c76ae8eade4ea"
        },
        "date": 1674814665724,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 16.011469592081063,
            "unit": "iter/sec",
            "range": "stddev: 0.0053754016797916875",
            "extra": "mean: 62.45522900000253 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 3.729295423100699,
            "unit": "iter/sec",
            "range": "stddev: 0.020010681096500196",
            "extra": "mean: 268.1471662999968 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 87.10657834804884,
            "unit": "iter/sec",
            "range": "stddev: 0.003130615468326437",
            "extra": "mean: 11.480189199997426 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 127.05912494363108,
            "unit": "iter/sec",
            "range": "stddev: 0.0007184463296019359",
            "extra": "mean: 7.870351699995125 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "github@schroedingerscat.org",
            "name": "Florian Dobener",
            "username": "domna"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "b9e22a80f7b5ee6777ce107233e505c1af82fe42",
          "message": "Adds pseudo dielectric dispersion (#115)\n\n* Adds pseudo dielectric dispersion\r\n\r\n* Fixes error message\r\n\r\n* Adds docstring\r\n\r\n* Adds tests for pseudo dielectric function\r\n\r\n* Adds functional test for pseudo dielectric\r\n\r\n* Adds more values for checking interpolation\r\n\r\n* Fix file docstring\r\n\r\n---------\r\n\r\nCo-authored-by: MarJMue <49639740+MarJMue@users.noreply.github.com>",
          "timestamp": "2023-01-30T11:08:52+01:00",
          "tree_id": "bdcbda5dd990fe54a3e573d8278a196a20233421",
          "url": "https://github.com/PyEllips/pyElli/commit/b9e22a80f7b5ee6777ce107233e505c1af82fe42"
        },
        "date": 1675073421375,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 25.416387526954306,
            "unit": "iter/sec",
            "range": "stddev: 0.0008343603537170424",
            "extra": "mean: 39.344694400000435 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 5.502358115354608,
            "unit": "iter/sec",
            "range": "stddev: 0.0212467337722975",
            "extra": "mean: 181.74026099999736 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 134.78823575283508,
            "unit": "iter/sec",
            "range": "stddev: 0.00039936023721555576",
            "extra": "mean: 7.4190451000021085 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 141.5376099611022,
            "unit": "iter/sec",
            "range": "stddev: 0.0029137322625180156",
            "extra": "mean: 7.065259899999887 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "github@schroedingerscat.org",
            "name": "Florian Dobener",
            "username": "domna"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "e8a0789bcac64962ec25f700fd2938af0ccc4207",
          "message": "Prevents refractive index dispersions from being summed (#113)\n\n* Adds unsummable dispersion\r\n\r\n* Replaces UnsummableDispersion with IndexDispersion\r\n\r\n* Lets IndexTable inherit from IndexDispersion\r\n\r\n* Raise error on adding of tabular dispersions\r\n\r\n* Offload add to table dispersion",
          "timestamp": "2023-01-30T11:09:08+01:00",
          "tree_id": "0e4daf423c4038681ee0287a79ff9d31cf9fd312",
          "url": "https://github.com/PyEllips/pyElli/commit/e8a0789bcac64962ec25f700fd2938af0ccc4207"
        },
        "date": 1675073440464,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 24.306605938521443,
            "unit": "iter/sec",
            "range": "stddev: 0.0011207043369197362",
            "extra": "mean: 41.14107920000407 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 6.633011984332232,
            "unit": "iter/sec",
            "range": "stddev: 0.018549035769544177",
            "extra": "mean: 150.76107240000312 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 144.8230600367822,
            "unit": "iter/sec",
            "range": "stddev: 0.00033074313350051326",
            "extra": "mean: 6.90497770000178 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 196.50934168076316,
            "unit": "iter/sec",
            "range": "stddev: 0.000057370318269309956",
            "extra": "mean: 5.088816599999291 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "committer": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "distinct": true,
          "id": "c7b8b0ebb01a4bebec28b27da35bfb23c21c89f5",
          "message": "Updates changelog",
          "timestamp": "2023-01-30T11:20:17+01:00",
          "tree_id": "e69e53886cc8cfb3c89cfa536bb20acceb7214ec",
          "url": "https://github.com/PyEllips/pyElli/commit/c7b8b0ebb01a4bebec28b27da35bfb23c21c89f5"
        },
        "date": 1675074113285,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 24.18567632004108,
            "unit": "iter/sec",
            "range": "stddev: 0.0008405792438358666",
            "extra": "mean: 41.34678670000085 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 5.848392239105182,
            "unit": "iter/sec",
            "range": "stddev: 0.016477557317958108",
            "extra": "mean: 170.98716349999847 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 146.32702272193268,
            "unit": "iter/sec",
            "range": "stddev: 0.00017659407339068727",
            "extra": "mean: 6.834007700001621 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 194.07543211320854,
            "unit": "iter/sec",
            "range": "stddev: 0.00030239718887784846",
            "extra": "mean: 5.152635700002861 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "committer": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "distinct": true,
          "id": "49a8425513b1a33391f924c3ee52ba3576887a47",
          "message": "Adds docs for pseudo dielectric function",
          "timestamp": "2023-01-30T17:57:42+01:00",
          "tree_id": "c7cf4d0eafa548c43218d3610b028f71a9be4076",
          "url": "https://github.com/PyEllips/pyElli/commit/49a8425513b1a33391f924c3ee52ba3576887a47"
        },
        "date": 1675097948281,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 24.82138802214519,
            "unit": "iter/sec",
            "range": "stddev: 0.0009981678445892541",
            "extra": "mean: 40.28783560000022 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 5.460221755145301,
            "unit": "iter/sec",
            "range": "stddev: 0.01538816688908846",
            "extra": "mean: 183.1427448999989 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 87.72598773688259,
            "unit": "iter/sec",
            "range": "stddev: 0.004199170292405157",
            "extra": "mean: 11.399130700007731 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 170.7658000843401,
            "unit": "iter/sec",
            "range": "stddev: 0.0004245580927965944",
            "extra": "mean: 5.855973499998868 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "committer": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "distinct": true,
          "id": "7d4700d54a9564419995f077e07215f766bc2519",
          "message": "Fixes docs for pseudo dielectric",
          "timestamp": "2023-01-30T18:50:30+01:00",
          "tree_id": "80c94d3987c8d02e63ddaabfc6e07a25be8702b8",
          "url": "https://github.com/PyEllips/pyElli/commit/7d4700d54a9564419995f077e07215f766bc2519"
        },
        "date": 1675101131914,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 21.591624948964167,
            "unit": "iter/sec",
            "range": "stddev: 0.0014625159754917654",
            "extra": "mean: 46.31425390000459 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 5.096145891168093,
            "unit": "iter/sec",
            "range": "stddev: 0.022539541756014445",
            "extra": "mean: 196.22672140000077 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 83.07370930018955,
            "unit": "iter/sec",
            "range": "stddev: 0.0015540886203173122",
            "extra": "mean: 12.037502699999436 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 144.75100084817012,
            "unit": "iter/sec",
            "range": "stddev: 0.0009545687795947455",
            "extra": "mean: 6.908415100002685 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "committer": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "distinct": true,
          "id": "f0e96d87bb612ff70f9f70005c3770bdf6804017",
          "message": "Use absolute path for logo",
          "timestamp": "2023-01-30T19:22:11+01:00",
          "tree_id": "f5314cc1893872e0a61bf5312e6f734b6effb51b",
          "url": "https://github.com/PyEllips/pyElli/commit/f0e96d87bb612ff70f9f70005c3770bdf6804017"
        },
        "date": 1675103015436,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 22.635753904879166,
            "unit": "iter/sec",
            "range": "stddev: 0.009045463858788157",
            "extra": "mean: 44.17789680000226 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 6.718958587864949,
            "unit": "iter/sec",
            "range": "stddev: 0.019695683110956312",
            "extra": "mean: 148.83258869999452 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 93.53245170142355,
            "unit": "iter/sec",
            "range": "stddev: 0.0031693923270367523",
            "extra": "mean: 10.691476400000965 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 193.03938955222407,
            "unit": "iter/sec",
            "range": "stddev: 0.0003136128584985848",
            "extra": "mean: 5.180289900002322 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "committer": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "distinct": true,
          "id": "1c96d2df8aa3898f426bb661eda6ccd473f0d0c3",
          "message": "Attempted fix for double-colon in rtd",
          "timestamp": "2023-02-02T19:51:00+01:00",
          "tree_id": "03a9f41a3961b4da63908e6faa673f3a85f1a4e5",
          "url": "https://github.com/PyEllips/pyElli/commit/1c96d2df8aa3898f426bb661eda6ccd473f0d0c3"
        },
        "date": 1675363945697,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 24.144425676845295,
            "unit": "iter/sec",
            "range": "stddev: 0.0006863549271563212",
            "extra": "mean: 41.41742750000503 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 6.691740865052007,
            "unit": "iter/sec",
            "range": "stddev: 0.022055941801015392",
            "extra": "mean: 149.43794449999643 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 144.87774448069405,
            "unit": "iter/sec",
            "range": "stddev: 0.00037683819959396093",
            "extra": "mean: 6.902371399999652 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 190.3505301206739,
            "unit": "iter/sec",
            "range": "stddev: 0.000630112338636019",
            "extra": "mean: 5.253465799995638 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "committer": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "distinct": true,
          "id": "4284972c18e9f88a777a6a5866913cf04ab644fd",
          "message": "Updates formatting according to black>=23",
          "timestamp": "2023-02-02T20:01:59+01:00",
          "tree_id": "5194d14e1c3ddc779e64a4f96fb728114898df17",
          "url": "https://github.com/PyEllips/pyElli/commit/4284972c18e9f88a777a6a5866913cf04ab644fd"
        },
        "date": 1675364600741,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 24.064694427151,
            "unit": "iter/sec",
            "range": "stddev: 0.0008998903180703523",
            "extra": "mean: 41.55465189999461 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 7.007089999290045,
            "unit": "iter/sec",
            "range": "stddev: 0.01885332480429234",
            "extra": "mean: 142.7125953999905 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 100.30329710977142,
            "unit": "iter/sec",
            "range": "stddev: 0.003369778657806504",
            "extra": "mean: 9.969762000002902 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 193.83558640703777,
            "unit": "iter/sec",
            "range": "stddev: 0.00006040491352932281",
            "extra": "mean: 5.1590114000021 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "committer": {
            "email": "florian.dobener@physik.hu-berlin.de",
            "name": "domna",
            "username": "domna"
          },
          "distinct": true,
          "id": "e752d132b4ac2d266b2b0e882700786adefc8e53",
          "message": "Use picture tag for pyElli image",
          "timestamp": "2023-02-02T20:16:33+01:00",
          "tree_id": "593d58a250ffb80ce93320bdcaf189c527c04914",
          "url": "https://github.com/PyEllips/pyElli/commit/e752d132b4ac2d266b2b0e882700786adefc8e53"
        },
        "date": 1675365482449,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 25.140578193975696,
            "unit": "iter/sec",
            "range": "stddev: 0.0009059796210667455",
            "extra": "mean: 39.776332600004594 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 6.906559156883001,
            "unit": "iter/sec",
            "range": "stddev: 0.01634792421271559",
            "extra": "mean: 144.78989860000127 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 137.00634370867888,
            "unit": "iter/sec",
            "range": "stddev: 0.0002808490069272809",
            "extra": "mean: 7.29893210000796 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 155.56839167638435,
            "unit": "iter/sec",
            "range": "stddev: 0.0019661298385167006",
            "extra": "mean: 6.428041000000917 msec\nrounds: 10"
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
          "id": "928df3cdf9ec4aebed671285801a7cd70400f5ff",
          "message": "Add Cauchy urbach dispersion (#117)\n\n* cauchy urbach model\r\n* Update to new IndexDispersion\r\n* CauchyUrbach: docs\r\n* CauchyUrbach: tests\r\n* add reference",
          "timestamp": "2023-02-06T09:16:09+01:00",
          "tree_id": "324f8181d46291f8450b45579a32c17f5513534b",
          "url": "https://github.com/PyEllips/pyElli/commit/928df3cdf9ec4aebed671285801a7cd70400f5ff"
        },
        "date": 1675671481070,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 20.7491175068336,
            "unit": "iter/sec",
            "range": "stddev: 0.002705486056715816",
            "extra": "mean: 48.19482080000057 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 5.023528580246969,
            "unit": "iter/sec",
            "range": "stddev: 0.02014217709430702",
            "extra": "mean: 199.06326479998597 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 118.55957420615394,
            "unit": "iter/sec",
            "range": "stddev: 0.0002977228207850642",
            "extra": "mean: 8.434578199995713 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 121.03435475438334,
            "unit": "iter/sec",
            "range": "stddev: 0.003025409155209766",
            "extra": "mean: 8.26211699999817 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "49699333+dependabot[bot]@users.noreply.github.com",
            "name": "dependabot[bot]",
            "username": "dependabot[bot]"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "2a83d2a349a622a34477230753f6c1a584668a9a",
          "message": "Bump ipython from 8.5.0 to 8.10.0 in /requirements (#121)\n\nBumps [ipython](https://github.com/ipython/ipython) from 8.5.0 to 8.10.0.\r\n- [Release notes](https://github.com/ipython/ipython/releases)\r\n- [Commits](https://github.com/ipython/ipython/compare/8.5.0...8.10.0)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: ipython\r\n  dependency-type: direct:production\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2023-02-11T09:03:42+01:00",
          "tree_id": "60a14383d19e64f23bbdc9539131408cb292ca31",
          "url": "https://github.com/PyEllips/pyElli/commit/2a83d2a349a622a34477230753f6c1a584668a9a"
        },
        "date": 1676102704764,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 25.09878121046426,
            "unit": "iter/sec",
            "range": "stddev: 0.0021073973868249813",
            "extra": "mean: 39.84257209999811 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 6.7745740099932075,
            "unit": "iter/sec",
            "range": "stddev: 0.017186070293828827",
            "extra": "mean: 147.61075730000073 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 143.5849689108566,
            "unit": "iter/sec",
            "range": "stddev: 0.0001651480913160131",
            "extra": "mean: 6.964517300002626 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 180.55066689560863,
            "unit": "iter/sec",
            "range": "stddev: 0.0006057016097709017",
            "extra": "mean: 5.538611499996193 msec\nrounds: 10"
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
          "id": "d4d5dd649b884192d9fbc9d39f18b489b31e9c38",
          "message": "RII Database: Filtering by range (#108)\n\n* Regex parsing of database\r\n* specify encoding\r\n* convert to correct dtypes\r\n* implement wavelength filtering for searches\r\n* allow more iterable types and improve readability\r\n* correct naming scheme for typevar",
          "timestamp": "2023-02-15T12:03:57+01:00",
          "tree_id": "51a5291f223e8e6fb601a9cf2afc26b4b971796b",
          "url": "https://github.com/PyEllips/pyElli/commit/d4d5dd649b884192d9fbc9d39f18b489b31e9c38"
        },
        "date": 1676459124970,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 25.384755469412237,
            "unit": "iter/sec",
            "range": "stddev: 0.001055281761989704",
            "extra": "mean: 39.3937219999998 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 6.1509026233088075,
            "unit": "iter/sec",
            "range": "stddev: 0.026726992558970805",
            "extra": "mean: 162.5777647999996 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 89.44975155285614,
            "unit": "iter/sec",
            "range": "stddev: 0.003420657907138816",
            "extra": "mean: 11.179460900001459 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 192.5554408031219,
            "unit": "iter/sec",
            "range": "stddev: 0.0001431214284540575",
            "extra": "mean: 5.1933095000023854 msec\nrounds: 10"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "github@schroedingerscat.org",
            "name": "Florian Dobener",
            "username": "domna"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "9dfac8999581a86c54bbb7e8017a73a22dff60ed",
          "message": "Update README.md",
          "timestamp": "2023-03-14T20:35:44+01:00",
          "tree_id": "64871d42112b86c45379eb0f31e5f21065a6e6fd",
          "url": "https://github.com/PyEllips/pyElli/commit/9dfac8999581a86c54bbb7e8017a73a22dff60ed"
        },
        "date": 1678822631324,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 24.358048028650913,
            "unit": "iter/sec",
            "range": "stddev: 0.0005852063263303797",
            "extra": "mean: 41.05419280000433 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 6.174339821202457,
            "unit": "iter/sec",
            "range": "stddev: 0.013841777245502968",
            "extra": "mean: 161.96063529999378 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 136.2861174396665,
            "unit": "iter/sec",
            "range": "stddev: 0.0012889140903867247",
            "extra": "mean: 7.337504499992065 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 171.396357727932,
            "unit": "iter/sec",
            "range": "stddev: 0.00147154901221948",
            "extra": "mean: 5.83442970000192 msec\nrounds: 10"
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
          "id": "09031b7f8cf8f9d1c56e7fd86c769afc3593f14d",
          "message": "Update discord link",
          "timestamp": "2023-03-22T17:35:48+01:00",
          "tree_id": "3c940c25f327f02bfea7d58379981c5d94dd2c47",
          "url": "https://github.com/PyEllips/pyElli/commit/09031b7f8cf8f9d1c56e7fd86c769afc3593f14d"
        },
        "date": 1679503051242,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_eig",
            "value": 20.533839877971623,
            "unit": "iter/sec",
            "range": "stddev: 0.006998511432555342",
            "extra": "mean: 48.70009730000788 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_expm",
            "value": 4.939042710237507,
            "unit": "iter/sec",
            "range": "stddev: 0.01958216224434646",
            "extra": "mean: 202.4683847999995 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver4x4_linear",
            "value": 106.54059760379116,
            "unit": "iter/sec",
            "range": "stddev: 0.002603168521269922",
            "extra": "mean: 9.386093399990614 msec\nrounds: 10"
          },
          {
            "name": "tests/benchmark_propagators_TiO2.py::test_solver2x2",
            "value": 131.93814027538684,
            "unit": "iter/sec",
            "range": "stddev: 0.0029201323442617825",
            "extra": "mean: 7.579309499988085 msec\nrounds: 10"
          }
        ]
      }
    ]
  }
}