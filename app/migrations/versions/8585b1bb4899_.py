"""empty message

Revision ID: 8585b1bb4899
Revises: 
Create Date: 2018-02-10 01:24:51.015271

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8585b1bb4899'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('game',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_game_name'), 'game', ['name'], unique=False)
    op.create_table('board_item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('shortname', sa.String(length=80), nullable=False),
    sa.Column('marked', sa.Boolean(), nullable=True),
    sa.Column('diff', sa.Integer(), nullable=True),
    sa.Column('game_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['game_id'], ['game.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_board_item_name'), 'board_item', ['name'], unique=False)
    op.create_index(op.f('ix_board_item_shortname'), 'board_item', ['shortname'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_board_item_shortname'), table_name='board_item')
    op.drop_index(op.f('ix_board_item_name'), table_name='board_item')
    op.drop_table('board_item')
    op.drop_index(op.f('ix_game_name'), table_name='game')
    op.drop_table('game')
    # ### end Alembic commands ###