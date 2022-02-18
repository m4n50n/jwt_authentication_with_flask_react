"""empty message

Revision ID: 126191cb014f
Revises: 2807edd385a2
Create Date: 2022-02-17 19:55:32.834938

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '126191cb014f'
down_revision = '2807edd385a2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(length=120),
               type_=sa.String(length=50),
               existing_nullable=False)
    op.alter_column('user', 'password',
               existing_type=sa.VARCHAR(length=80),
               type_=sa.String(length=15),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'password',
               existing_type=sa.String(length=15),
               type_=sa.VARCHAR(length=80),
               existing_nullable=False)
    op.alter_column('user', 'email',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=120),
               existing_nullable=False)
    # ### end Alembic commands ###
