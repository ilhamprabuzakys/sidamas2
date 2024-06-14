from csv import DictReader
import csv
from pathlib import Path
from django.contrib.auth.models import User
from django.core.management import BaseCommand
from import_export.fields import ObjectDoesNotExist
from termcolor import colored, cprint

from users.models import Profile, Satker, SatkerBNNP

class Command(BaseCommand):
    help = "Generate data user BNNP"
    separator = '-----'

    processed_count = 0
    total_count = SatkerBNNP.objects.count()
    list_satker = SatkerBNNP.objects.all()

    duplicate_entry = False
    duplicate_entry_row = []
    duplicate_count = 0
    iteration = 0

    def add_arguments(self, parser):
        parser.add_argument('--prevent_duplicates', type=int, default=1, help='Prevent duplicate entry')

    def get_hasil_keseluruhan(self):
        print(f'==HASIL KESELURUHAN ==\n{self.separator}')
        print('Processed \t:', colored(self.processed_count, 'green' if self.processed_count > 0 else 'red'))
        print('Total BNNP \t:', colored(self.total_count, 'white', attrs=['bold']))
        print('Duplicate Entry :', colored(self.duplicate_entry, 'green' if self.duplicate_entry else 'red'))
        print('Duplicate Row :', self.duplicate_entry_row)
        print('Duplicate Count :', colored(self.duplicate_count, 'yellow'))
        print('======================')

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('\nProses dimulai!\n'))

        prevent_duplicates = options['prevent_duplicates']

        try:
            print('Total satuan kerja BNNP :', self.total_count)

            text = 'menghiraukan' if prevent_duplicates == 1 else 'menghalau duplikasi'
            print(f'Proses dimulai dengan {text}')

            for satker in self.list_satker:
                self.iteration += 1
                no = f'({self.iteration} / {self.total_count})'

                if prevent_duplicates == 1 and satker.jumlah_profil != 0:
                    print(f"{colored('EXIST :', 'yellow')} Satuan Kerja {colored(satker.nama_satker, attrs=['bold'])} sudah memiliki perwakilan user ...")
                    pass
                else:
                    data = {
                        'first_name': satker.nama_satker,
                        'username': satker.nama_satker.lower().replace(" ", "_"),
                        'password': satker.nama_satker.lower().replace(" ", "_"),
                        'is_staff': True,
                        'is_superuser': False,
                    }

                    user = User.objects.create_user(**data)
                    user.set_password(data['password'])
                    user.save()

                    Profile.objects.create(user=user, satker_id=satker.satker_id)

                    self.processed_count += 1

                    print(f"{colored(no, attrs=['bold'])}: {colored('SUCCESS :', 'green')} Data user untuk Satuan Kerja {colored(user.first_name, attrs=['bold'])} berhasil dibuat ... ")
        except Exception as e:
            print(f"{colored(e, 'red', attrs=['bold'])}")
            self.stdout.write(self.style.ERROR(f'\nProses dihentikan karena terjadi error!\n'))
            return
        finally:
            self.stdout.write(self.style.SUCCESS('\nProses telah selesai\n'))
            return
