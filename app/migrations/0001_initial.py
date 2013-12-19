# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Adding model 'Project'
        db.create_table(u'app_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'app', ['Project'])

        # Adding model 'Table'
        db.create_table(u'app_table', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(related_name='app_table_project',
                                                                              to=orm['app.Project'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('order', self.gf('django.db.models.fields.SmallIntegerField')()),
        ))
        db.send_create_signal(u'app', ['Table'])

        # Adding model 'Field'
        db.create_table(u'app_field', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('table', self.gf('django.db.models.fields.related.ForeignKey')(related_name='app_field_table',
                                                                            to=orm['app.Table'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('primary', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('null', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('type', self.gf('django.db.models.fields.IntegerField')(max_length=2)),
            ('insert', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'app', ['Field'])

        # Adding model 'ForeignKey'
        db.create_table(u'app_foreignkey', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('origin', self.gf('django.db.models.fields.related.ForeignKey')(related_name='app_foreign_key_origin',
                                                                             to=orm['app.Field'])),
            ('destiny', self.gf('django.db.models.fields.related.ForeignKey')(related_name='app_foreign_key_destiny',
                                                                              to=orm['app.Field'])),
        ))
        db.send_create_signal(u'app', ['ForeignKey'])


    def backwards(self, orm):
        # Deleting model 'Project'
        db.delete_table(u'app_project')

        # Deleting model 'Table'
        db.delete_table(u'app_table')

        # Deleting model 'Field'
        db.delete_table(u'app_field')

        # Deleting model 'ForeignKey'
        db.delete_table(u'app_foreignkey')


    models = {
        u'app.field': {
            'Meta': {'object_name': 'Field'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insert': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'null': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'primary': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'table': ('django.db.models.fields.related.ForeignKey', [],
                      {'related_name': "'app_field_table'", 'to': u"orm['app.Table']"}),
            'type': ('django.db.models.fields.IntegerField', [], {'max_length': '2'})
        },
        u'app.foreignkey': {
            'Meta': {'object_name': 'ForeignKey'},
            'destiny': ('django.db.models.fields.related.ForeignKey', [],
                        {'related_name': "'app_foreign_key_destiny'", 'to': u"orm['app.Field']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'origin': ('django.db.models.fields.related.ForeignKey', [],
                       {'related_name': "'app_foreign_key_origin'", 'to': u"orm['app.Field']"})
        },
        u'app.project': {
            'Meta': {'object_name': 'Project'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'app.table': {
            'Meta': {'object_name': 'Table'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'order': ('django.db.models.fields.SmallIntegerField', [], {}),
            'project': ('django.db.models.fields.related.ForeignKey', [],
                        {'related_name': "'app_table_project'", 'to': u"orm['app.Project']"})
        }
    }

    complete_apps = ['app']