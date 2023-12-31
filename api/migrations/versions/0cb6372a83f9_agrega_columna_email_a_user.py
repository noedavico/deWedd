"""Agrega columna email a User

Revision ID: 0cb6372a83f9
Revises: 
Create Date: 2023-08-23 19:51:46.193452

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0cb6372a83f9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('is_active', sa.Boolean(), nullable=False))
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=80),
               nullable=False)
        batch_op.alter_column('username',
               existing_type=sa.VARCHAR(length=80),
               type_=sa.String(length=150),
               nullable=False)
        batch_op.create_unique_constraint('uq_user_email', ['email'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.alter_column('username',
               existing_type=sa.String(length=150),
               type_=sa.VARCHAR(length=80),
               nullable=True)
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=80),
               nullable=True)
        batch_op.drop_column('is_active')
        batch_op.drop_column('email')

    # ### end Alembic commands ###
