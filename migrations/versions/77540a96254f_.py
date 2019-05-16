"""empty message

Revision ID: 77540a96254f
Revises: 
Create Date: 2019-05-16 02:53:09.818867

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '77540a96254f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.drop_index('user_id', table_name='users')
    op.drop_table('users')
    op.drop_table('MyGuests')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('MyGuests',
    sa.Column('id', mysql.INTEGER(display_width=6, unsigned=True), autoincrement=True, nullable=False),
    sa.Column('firstname', mysql.VARCHAR(length=30), nullable=False),
    sa.Column('lastname', mysql.VARCHAR(length=30), nullable=False),
    sa.Column('email', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('reg_date', mysql.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('users',
    sa.Column('user_id', mysql.BIGINT(display_width=20, unsigned=True), autoincrement=True, nullable=False),
    sa.Column('username', mysql.VARCHAR(length=30), nullable=False),
    sa.Column('password', mysql.VARCHAR(length=30), nullable=False),
    sa.Column('email', mysql.VARCHAR(length=30), nullable=False),
    sa.Column('gender', mysql.VARCHAR(length=30), nullable=False),
    sa.PrimaryKeyConstraint('user_id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_index('user_id', 'users', ['user_id'], unique=True)
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###