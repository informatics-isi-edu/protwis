ps aux | grep manage.py | awk '{print $2}'
nohup nice python3 manage.py runsslserver  0.0.0.0:8000  --certificate /home/anoopk/star_misd_isi_edu.crt --key /home/anoopk/star_misd_isi_edu_npp.key > logs/nohup.out 2>&1 &
