<h1>Nomadgram</h1>
            <h2>Instagram clone with python and javascript</h2>
            <ul>
                <li>
                    <h3>requirement</h3>
                    <ul>
                        <li>setting: cookiecutter, pipenv, install requirement</li>
                        <li>server: python3.0, django2.0, postgreSQL9.6</li>
                        <li>front:javascript, reactjs</li>
                        <li>app:react-native, android studio</li>
                    </ul>   
                </li>
                <li>
                    <h4>setting</h4>
                    <ul>
                        <li>
                            cookiecutter: 쿠키커터는 장고, 파이썬 서버 개발을 도와주는 보일러 플레이트 격 프로그램으로
                            별도의 template 없이 개발한 API의 결과 data를 프론트로 확인하며 개발할 수 있습니다.
                            pip install cookiecutter을 통해 쿠키커터 프로그램을 설치한 뒤 필요한 쿠키를 쿠키컷합니다.
                            <b>cookiecutter https://github.com/pydanny/cookiecutter-django</b>을 통해 장고 개발자를 위한 쿠키를 쿠키컷합시다.
                            쿠키컷 과정에서 프로젝트의 이름, 개발자 이메일 등 기본적인 내용 및 필요 요건을 기입하면 됩니다.
                        </li>
                        <li>pipenv: 가상환경에서 개발을 진행합니다. 우리에게 필요한 django, python 등을 다른 개발 환경과
                            격리하고 우리의 nomadgram에서만 사용하기 위한 가상공간입니다.
                            pipenv 기능 자체는 python을 설치하고 pip를 설치했다면 <b>pip install pipenv</b> 명령어를 통해 설치 가능하며
                            개별 가상환경을 만들기 위해서는 해당 프로젝트 경로에서 <b>pipenv --three</b> 명령어를 통해 가능합니다.
                            이후 우리가 가상환경에서 설치하는 것들은 <b>pipenv install django</b> 등의 명령어를 통해 합니다. 
                        </li>
                        <li>
                            install requirement: 쿠키커터를 사용하면 필요한 기본적인 프로그램들을 requirements폴더의 local.txt 파일 참조해서
                            설치할 수 있습니다. 이는 <b>pipenv install -r requirements/local.txt</b> 명령어로 한번에 설치가능합니다.
                        </li>
                    </ul>
                </li>
                <li>
                    <h4>server</h4>
                    <ul>
                        <li>python3.0: 파이썬은 3버전 이상을 사용합니다. python.org 홈페이지에서 OS에 맞는 것을 설치합니다.</li>
                        <li>
                            django2.0: 장고는 2버전 이상을 사용합니다. 앞선 intall requirement 과정에서 설치가 완료됩니다.
                        </li>
                        <li>
                            postgreSQL9.6: DATABASE는 postgre를 사용합니다. django는 다양한 데이터베이스를 호환하기 때문에
                            혹시 mysql등 다른 데이터베이스를 사용하고 싶다면 셋팅해서 사용할 수 있습니다.
                        </li>
                    </ul>
                </li>
                <li>
                    <h4>front</h4>
                    <ul>
                        <li>javascript: 우리가 만들 인스타그램 웹, 앱은 자바스크립트를 기반으로 디자인 됩니다. 
                            자바스크립트를 기반으로한 라이브러리와 프레임워크를 활용하기도 합니다.
                        </li>
                        <li>
                            reactjs: 리액트는 가장 핫한 자바스크립트 라이브러리입니다. 리액트를 이용해 DOM을 효과적으로 제어하고
                            컴포넌트를 구분해 웹을 디자인 해볼 것입니다. 더불어 서버에서 응답된 데이터를 사용자가 사용하기 쉽게
                            설계합니다.
                        </li>
                    </ul>
                </li>
                <li>
                    <h4>app</h4>
                    <ul>
                        <li>
                        react-native: 리액트 네이티브는 우리가 만든 웹을 앱으로 사용할 수 있도록 해주는 것입니다. 
                        네이티브 앱을 개발을 해보며 카메라, GPS 등을 제어할 수 있습니다.
                    </li> 
                        <li>
                            android studio: 안드로이드 스튜디오는 우리가 만든 앱을 테스트하기 위해 사용합니다.
                            가상의 휴대폰 화면을 띄운 시뮬레이터를 활용할 수 있습니다.
                        </li> 
                  </ul>
                </li>
            </ul>      
             <h3>Project structure</h3>
             쿠키커터를 하고 필요 프로그램 설치, 기본적인 우리가 사용할 언어를 알아봤습니다. 이제 프로젝트의 구조를 알아봅시다.
             <ul>
                 <li>
                     <h4>config</h4>
                     우리가 만든 프로젝트에는 config 폴더가 있습니다. 이는 우리 프로젝트의 중심부 커맨드센터 역할을 하는 폴더입니다.
                     <ul>
                         <li>
                             settings: settings폴더는 다양한 설정을 하는 곳입니다. 이 폴더에는 base.py, local.py 등 다양한 설정 파일이 있습니다. Time zone, database, app인스톨 등을 기입하는 파일로 기본적인 세팅은 여기서한다고 생각하면됩니다.
                         </li>
                         <li>
                             urls.py: 이 파일은 우리 프로젝트의 API url을 기입하는 곳입니다. 만약 우리가 이미지를 등록하는 기능을 만든다면
                             사용자는 이 기능을 사용하기 위해 url을 통해 서버에 요청을 보내게 됩니다. 이 url을 보고 우리의 서버는 알맞은 응답을 할 것입니다.
                         </li>
                     </ul>
                 </li>
                 <li>
                     <h4>nomadgram</h4>
                     우리가 만든 nomadgram프로젝트 안에는 또 nomadgram폴더가 있습니다. 이는 세부적으로 우리가 만들 기능들을
                     넣는 폴더입니다. <b>django-admin startapp 앱이름</b> 명령어를 통해 만든 폴더가 여기에 저장됩니다.
                     우리가 만들 인스타그램은 이미지와 관련된 기능을 담는 images앱, 사용자와 관련된 기능을 담는 users앱
                     알람 기능을 담는 notifications앱 등이 있습니다.
                     더불어 templates폴더도 생성되는데 이 폴더는 서버 설계가 끝난 뒤 프론트를 제작할 공간입니다. 
                 </li>
                 우리는 config와 nomadgram 두 폴더에 있는 파일의 내용을 바꾸어 프로젝트를 완성할 것입니다.
             </ul>
