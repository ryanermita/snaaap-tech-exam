db.auth('root', 'example')

db.createUser({
  user: 'snaaap_user',
  pwd: 'snaaap_password',
  roles: [
    {
      role: 'readWrite',
      db: 'snaaap_tech_exam_db',
    },
  ],
});