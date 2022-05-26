"""employers table

Revision ID: 6b2447c8a98b
Revises: 0cdb995886a8
Create Date: 2022-05-26 14:40:14.242212

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b2447c8a98b'
down_revision = '0cdb995886a8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('surname', sa.String(length=64), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('date_employment', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_employer_age'), 'employer', ['age'], unique=False)
    op.create_index(op.f('ix_employer_date_employment'), 'employer', ['date_employment'], unique=False)
    op.create_index(op.f('ix_employer_name'), 'employer', ['name'], unique=False)
    op.create_index(op.f('ix_employer_surname'), 'employer', ['surname'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_employer_surname'), table_name='employer')
    op.drop_index(op.f('ix_employer_name'), table_name='employer')
    op.drop_index(op.f('ix_employer_date_employment'), table_name='employer')
    op.drop_index(op.f('ix_employer_age'), table_name='employer')
    op.drop_table('employer')
    # ### end Alembic commands ###
